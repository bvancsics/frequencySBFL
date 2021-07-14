

class AllFourMetrics:
    def __init__(self, coverageData):
        self.hit_results = SBFLFourMetrics(coverageData.graphContainer.hit_cov_graph, coverageData, False)
        self.unique_results = SBFLFourMetrics(coverageData.graphContainer.unique_cov_graph, coverageData, True)
        self.naive_results = SBFLFourMetrics(coverageData.graphContainer.naive_cov_graph, coverageData, True)


class SBFLFourMetrics:
    def __init__(self, graph, coverageData, is_weighted):
        self.results = self.get_four_metrics(graph, coverageData, is_weighted)

    def get_four_metrics(self, graph, coverageData, is_weighted):
        if is_weighted:
            return self.get_count_four_metrics(graph, coverageData)
        else:
            return self.get_hit_four_metrics(graph, coverageData)

    @staticmethod
    def get_hit_four_metrics(graph, coverageData):
        results = {}
        for method in set(coverageData.methodNames):
            covered_tests = set(list(graph.neighbors(method)))
            ef = len(covered_tests.intersection(set(coverageData.testResults.failed_tests)))
            ep = len(covered_tests.intersection(set(coverageData.testResults.passed_tests)))
            nf = len(coverageData.testResults.failed_tests) - ef
            np = len(coverageData.testResults.passed_tests) - ep
            results[method] = FourMetric(ef, ep, nf, np)
        return results

    def get_count_four_metrics(self, graph, coverageData):
        weight_from_test = self.weight_from_tests(graph, coverageData.testResults.pass_failed_dict.keys())
        results = {}
        for method in set(coverageData.methodNames):
            covered_tests = set(list(graph.neighbors(method)))
            failed_cov_test = covered_tests.intersection(set(coverageData.testResults.failed_tests))
            passed_cov_test = covered_tests.intersection(set(coverageData.testResults.passed_tests))

            failed_NOT_cov_test = set(coverageData.testResults.failed_tests)-set(failed_cov_test)
            passed_NOT_cov_test = set(coverageData.testResults.passed_tests)-set(passed_cov_test)

            ef = float(sum([graph[method][f_test]["weight"] for f_test in failed_cov_test]))
            ep = float(sum([graph[method][p_test]["weight"] for p_test in passed_cov_test]))
            nf = float(sum([weight_from_test[f_n_test] for f_n_test in failed_NOT_cov_test]))/float(int(len(coverageData.methodNames))-1)
            np = float(sum([weight_from_test[p_n_test] for p_n_test in passed_NOT_cov_test]))/float(int(len(coverageData.methodNames))-1)
            results[method] = FourMetric(ef, ep, nf, np)
        return results

    @staticmethod
    def weight_from_tests(graph, tests):
        weights={}
        for test in tests:
            weights[test] = sum([graph[method][test]["weight"] for method in graph.neighbors(test)])
        return weights


class FourMetric:
    def __init__(self, ef, ep, nf, np):
        self.ef = ef
        self.ep = ep
        self.nf = nf
        self.np = np
