import os
import networkx as nx
import test_results


class Coverage():
    def __init__(self, cov_folder, nameMapping=None):
        self.cov_folder = os.path.abspath(cov_folder)
        self.testResults = test_results.PassFailed(os.path.abspath(cov_folder))
        self.fixed_methods = set()
        self.testNames = self.get_testNames(os.path.abspath(cov_folder))
        self.methodNames = self.get_methodNames(nameMapping)
        self.IDmapper = self.read_nameMapping(nameMapping)
        self.chain_list = list()
        self.cov_graph = nx.Graph()


    def read_nameMapping(self, nameMapping):
        mapping = {}
        with open(nameMapping, 'r') as file:
            for line in file:
                parts = line.strip().split(':')
                assert len(parts) == 2
                id = int(parts[0])
                name = parts[1]
                mapping[id] = name
                mapping[-id] = name
        return mapping


    def get_methodNames(self, nameMapping):
        methods = list()
        with open(nameMapping, 'r') as file:
            for line in file:
                parts = line.strip().split(':')
                assert len(parts) == 2
                methods.append(parts[1])
        return methods


    def get_testNames(self, cov_folder):
        test_names = set()
        for r, d, f in os.walk(cov_folder):
            for file in f:
                if file.endswith(".trc"):
                    test_names.add(file.split("-")[0])
        return list(test_names)


    def set_coverage_data(self, change, bugID):
        self.get_fixed_methods(change, bugID)
        self.get_chain_graph()
        self.testResults.set_number_of_tests()


    def get_chain_graph(self):
        for r, d, f in os.walk(self.cov_folder):
            for file in f:
                if file.endswith(".trc"):
                    test_name = file.split("-")[0]
                    file_path = os.path.join(r, file)
                    for chain, count in self.read_chain(file_path, endianness='big'):
                        for cov_method in chain:
                            if not self.cov_graph.has_edge(test_name, self.IDmapper[cov_method]):
                                self.cov_graph.add_edge(test_name, self.IDmapper[cov_method], weight=0)
                            self.cov_graph[test_name][self.IDmapper[cov_method]]["weight"] += 1


    def read_chain(self, file_path, endianness='big'):
        with open(file_path, 'rb') as file:
            for item in self.read_chain_from_buffer(file, endianness=endianness):
                yield item

    def read_chain_from_buffer(self, buffer, mapping=None, endianness='big'):
        while True:
            chunk = buffer.read(4)
            if not chunk:
                break

            length = int.from_bytes(chunk, endianness, signed=True)
            if length <= 0:
                raise OverflowError('Length must be larger than zero (pos:{})'.format(buffer.tell()))

            chain = []
            for i in range(length):
                chunk = buffer.read(2)
                if not chunk:
                    raise IOError('Unexpected end of file: missing element of chain (pos:{})'.format(buffer.tell()))

                id = int.from_bytes(chunk, endianness, signed=True)
                if id < 0:
                    raise OverflowError('Code element id cannot be negative (pos:{})'.format(buffer.tell()))

                if mapping:
                    chain.append(mapping[id])
                else:
                    chain.append(id)

            chunk = buffer.read(8)
            if not chunk:
                raise IOError('Unexpected end of file: missing count value (pos:{})'.format(buffer.tell()))

            count = int.from_bytes(chunk, endianness, signed=True)
            if count <= 0:
                raise OverflowError('Count must be larger than zero (pos:{})'.format(buffer.tell()))
            yield (chain, count)


    def get_fixed_methods(self, change_file, bugID):
        with open(change_file, 'r') as infile:
            for line in infile:
                if line.startswith(str(bugID)+"b:") and int(line.split("\n")[0].split(":")[1]) != 0:
                    self.fixed_methods.add(line.split("\n")[0].split(":")[2])
