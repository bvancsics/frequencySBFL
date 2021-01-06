import os

results_dict = {"PASS": 1, "FAIL": 0}

class PassFailed():
    def __init__(self, cov_folder):
        self.pass_failed_dict = self.read_pass_failed_data(cov_folder)
        self.number_of_failed = 0
        self.number_of_pass = 0
        self.failed_tests = self.read_failed_tests(cov_folder)
        self.passed_tests = self.read_passed_tests(cov_folder)


    def read_pass_failed_data(self, cov_folder):
        pass_failed_dict={}
        for r, d, f in os.walk(cov_folder):
            for file in f:
                if file.endswith(".trc"):
                    test_name = file.split("-")[0]
                    result = results_dict[file.split("-")[1].split(".")[0]]
                    pass_failed_dict[test_name] = result
        return pass_failed_dict


    def read_passed_tests(self, cov_folder):
        passed_tests = list()
        for r, d, f in os.walk(cov_folder):
            for file in f:
                if file.endswith(".trc"):
                    test_name = file.split("-")[0]
                    result = results_dict[file.split("-")[1].split(".")[0]]
                    if result == 1 and test_name not in passed_tests:
                        passed_tests.append(test_name)
        return passed_tests

    def read_failed_tests(self, cov_folder):
        failed_tests = list()
        for r, d, f in os.walk(cov_folder):
            for file in f:
                if file.endswith(".trc"):
                    test_name = file.split("-")[0]
                    result = results_dict[file.split("-")[1].split(".")[0]]
                    if result == 0 and test_name not in failed_tests:
                        failed_tests.append(test_name)
        return failed_tests

    def set_number_of_tests(self):
        self.calc_number_of_failed()
        self.calc_number_of_pass()


    def calc_number_of_failed(self):
        for test, res in self.pass_failed_dict.items():
            if int(res) == int(0):
                self.number_of_failed += 1


    def calc_number_of_pass(self):
        for test, res in self.pass_failed_dict.items():
            if int(res) == int(1):
                self.number_of_pass += 1


    def covered_failed_tests(self, covered_tests):
        failed = 0
        for test in covered_tests:
            if self.pass_failed_dict[test] == int(0):
                failed += 1
        return failed


    def covered_passed_tests(self, covered_tests):
        passed = 0
        for teszt in covered_tests:
            if self.pass_failed_dict[teszt] == int(1):
                passed += 1
        return passed
