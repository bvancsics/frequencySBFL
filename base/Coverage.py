import os
import networkx as nx
from base import TestResults
from base import FourMetrics


class CoverageGraphContainer:
    def __init__(self, methods, tests):
        self.hit_cov_graph = self.init_test_method_graph(methods, tests)
        self.naive_cov_graph = self.init_test_method_graph(methods, tests)
        self.unique_cov_graph = self.init_test_method_graph(methods, tests)

    @staticmethod
    def init_test_method_graph(methods, tests):
        graph = nx.Graph()
        for method in methods:
            graph.add_node(method)
        for test in tests:
            graph.add_node(test)
        return graph


class Coverage:
    def __init__(self, naive_folder, naive_mapper, unique_folder, unique_mapper):
        self.naive_folder = None if naive_folder is None else os.path.abspath(naive_folder)
        self.naive_mapper = self.get_IDMapper(naive_mapper)
        self.unique_folder = None if unique_folder is None else os.path.abspath(unique_folder)
        self.unique_mapper = self.get_IDMapper(unique_mapper)

        self.testResults = TestResults.PassFailed(os.path.abspath(naive_folder))
        self.fixed_methods = set()
        self.testNames = self.get_testNames(os.path.abspath(naive_folder))
        self.methodNames = self.get_methodNames(naive_mapper)

        self.chain_list = list()
        self.graphContainer = None
        self.fourMetrics = None


    @staticmethod
    def get_IDMapper(nameMap_file):
        mapping = {}
        if nameMap_file is None:
            return mapping

        with open(nameMap_file, 'r') as file:
            for line in file:
                parts = line.strip().split(':')
                assert len(parts) == 2
                id = int(parts[0])
                name = parts[1]
                mapping[id] = name
                mapping[-id] = name
        return mapping

    @staticmethod
    def get_methodNames(nameMap_file):
        methods = list()
        with open(nameMap_file, 'r') as file:
            for line in file:
                parts = line.strip().split(':')
                assert len(parts) == 2
                methods.append(parts[1])
        return methods

    @staticmethod
    def get_testNames(cov_folder):
        test_names = set()
        for r, d, f in os.walk(cov_folder):
            for file in f:
                if file.endswith(".trc"):
                    test_names.add(file.split("-")[0])
        return list(test_names)


    def set_coverage_data(self, change, bugID):
        self.graphContainer = CoverageGraphContainer(self.methodNames, self.testResults.pass_failed_dict.keys())
        self.get_fixed_methods(change, bugID)
        self.get_graph()
        self.testResults.set_number_of_tests()
        self.fourMetrics = FourMetrics.AllFourMetrics(self)


    def get_graph(self):
        if self.unique_folder is not None:
            self.get_unique_graph()

        if self.naive_folder is not None:
            self.get_hit_graph()
            self.get_naive_graph()


    def get_hit_graph(self):
        for r, d, f in os.walk(self.naive_folder):
            for file in f:
                if file.endswith(".trc"):
                    test_name = file.split("-")[0]
                    file_path = os.path.join(r, file)
                    for cov_method, count in self.read_count(file_path, endianness='big'):
                        if not self.graphContainer.hit_cov_graph.has_edge(test_name, self.naive_mapper[cov_method]):
                            self.graphContainer.hit_cov_graph.add_edge(test_name, self.naive_mapper[cov_method], weight=1)

    def get_naive_graph(self):
        for r, d, f in os.walk(self.naive_folder):
            for file in f:
                if file.endswith(".trc"):
                    test_name = file.split("-")[0]
                    file_path = os.path.join(r, file)
                    for cov_method, count in self.read_count(file_path, endianness='big'):
                        if not self.graphContainer.naive_cov_graph.has_edge(test_name, self.naive_mapper[cov_method]):
                            self.graphContainer.naive_cov_graph.add_edge(test_name, self.naive_mapper[cov_method], weight=0)
                        self.graphContainer.naive_cov_graph[test_name][self.naive_mapper[cov_method]]["weight"] += count

    def get_unique_graph(self):
        for r, d, f in os.walk(self.unique_folder):
            for file in f:
                if file.endswith(".trc"):
                    test_name = file.split("-")[0]
                    file_path = os.path.join(r, file)
                    for chain, count in self.read_chain(file_path, endianness='big'):
                        for cov_method in chain:
                            if not self.graphContainer.unique_cov_graph.has_edge(test_name, self.unique_mapper[cov_method]):
                                self.graphContainer.unique_cov_graph.add_edge(test_name, self.unique_mapper[cov_method], weight=0)
                            self.graphContainer.unique_cov_graph[test_name][self.unique_mapper[cov_method]]["weight"] += 1


    def read_chain(self, file_path, endianness='big'):
        with open("\\\\?\\" + file_path, 'rb') as file:
            for item in self.read_chain_from_buffer(file, endianness=endianness):
                yield item

    def read_count(self, file, endianness='big'):
        with open("\\\\?\\" + file, 'rb') as file:
            for item in self.read_count_from_buffer(file, endianness=endianness):
                yield item

    def read_count_from_buffer(self, buffer, mapping=None, endianness='big'):
        while True:
            chunk = buffer.read(2)
            if not chunk:
                break

            id = int.from_bytes(chunk, endianness, signed=True)
            if id < 0:
                raise OverflowError('Code element id cannot be negative (pos:{})'.format(buffer.tell()))
            chunk = buffer.read(8)

            if not chunk:
                raise IOError('Unexpected end of file: missing count value (pos:{})'.format(buffer.tell()))
            count = int.from_bytes(chunk, endianness, signed=True)

            if count <= 0:
                raise OverflowError('Count must be larger than zero (pos:{})'.format(buffer.tell()))

            if mapping:
                yield (mapping[id], count)
            else:
                yield (id, count)


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
        if (change_file.count("Time") or
                change_file.count("Mockito") or
                change_file.count("Chart") or
                change_file.count("Lang") or
                change_file.count("Math") or
                change_file.count("Closure")):
            with open(change_file, 'r') as infile:
                for line in infile:
                    if line.startswith(str(bugID)+"b:") and int(line.split("\n")[0].split(":")[1]) != 0:
                        self.fixed_methods.add(line.split("\n")[0].split(":")[2])
        else:
            with open(change_file, 'r') as infile:
                for line in infile:
                    if line.startswith(str(bugID)):
                        self.fixed_methods.add(line.split("\n")[0].split(":")[2])
