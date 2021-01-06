import math



class Score():
    def __init__(self, metricName, coverageData):
        self.metricName = metricName
        self.score = self.set_score(metricName, coverageData)


    def set_score(self, metricName, coverageData):
        if metricName == "Barinel":
            metric = SBFLScore(coverageData)
            return metric.set_barinel(coverageData)
        elif metricName == "Barinel-C":
            metric = SBFLScore(coverageData)
            return metric.set_barinel_2(coverageData)
        elif metricName == "Jaccard":
            metric = SBFLScore(coverageData)
            return metric.set_jaccard(coverageData)
        elif metricName == "Jaccard-C":
            metric = SBFLScore(coverageData)
            return metric.set_jaccard_2(coverageData)
        elif metricName == "Ochiai":
            metric = SBFLScore(coverageData)
            return metric.set_ochiai(coverageData)
        elif metricName == "Ochiai-C":
            metric = SBFLScore(coverageData)
            return metric.set_ochiai_2(coverageData)
        elif metricName == "Russell-Rao":
            metric = SBFLScore(coverageData)
            return metric.set_russell_rao(coverageData)
        elif metricName == "Russell-Rao-C":
            metric = SBFLScore(coverageData)
            return metric.set_russell_rao_2(coverageData)
        elif metricName == "Sorensen-Dice":
            metric = SBFLScore(coverageData)
            return metric.set_sorensen_dice(coverageData)
        elif metricName == "Sorensen-Dice-C":
            metric = SBFLScore(coverageData)
            return metric.set_sorensen_dice_2(coverageData)


class SBFLScore():
    def __init__(self, coverageData):
        self.score = self.init_score(coverageData)

    def init_score(self, coverageData):
        score = {}
        for m in coverageData.methodNames:
            score[m] = 0.0
        return score

    def set_barinel(self, coverageData):
        methods = set(coverageData.methodNames).intersection(set(list(coverageData.cov_graph.nodes())))
        for method in methods:
            covered_tests = set(list(coverageData.cov_graph.neighbors(method)))
            ef = len(covered_tests.intersection(set(coverageData.testResults.failed_tests)))
            ep = len(covered_tests.intersection(set(coverageData.testResults.passed_tests)))

            tag1 = float(ef)
            tag2 = float(ef)+float(ep)
            if float(tag1)==0.0 or float(tag2)==0.0:
                self.score[method] = 0.0
            else:
                self.score[method] = float(tag1) / float(tag2)
        return self.score


    def set_barinel_2(self, coverageData):
        methods = set(coverageData.methodNames).intersection(set(list(coverageData.cov_graph.nodes())))
        for method in methods:
            covered_tests = set(list(coverageData.cov_graph.neighbors(method)))
            failed_cov_test = covered_tests.intersection(set(coverageData.testResults.failed_tests))
            fw = float(sum([coverageData.cov_graph[method][f_test]["weight"] for f_test in failed_cov_test]))

            tag1 = float(fw)
            tag2 = float(len(covered_tests))
            if float(tag1)==0.0 or float(tag2)==0.0:
                self.score[method] = 0.0
            else:
                self.score[method] = float(tag1) / float(tag2)
        return self.score


    def set_ochiai(self, coverageData):
        methods = set(coverageData.methodNames).intersection(set(list(coverageData.cov_graph.nodes())))
        for method in methods:
            covered_tests = set(list(coverageData.cov_graph.neighbors(method)))
            ef = len(covered_tests.intersection(set(coverageData.testResults.failed_tests)))
            ep = len(covered_tests.intersection(set(coverageData.testResults.passed_tests)))
            nf = len(coverageData.testResults.failed_tests) - ef

            tag1 = float(ef)
            tag2 = float(float(ef)+float(nf))*float(float(ef)+float(ep))
            if float(tag1)==0.0 or float(tag2)==0.0:
                self.score[method] = 0.0
            else:
                self.score[method] = float(tag1) / float(math.sqrt(float(tag2)))
        return self.score


    def set_ochiai_2(self, coverageData):
        methods = set(coverageData.methodNames).intersection(set(list(coverageData.cov_graph.nodes())))
        for method in methods:
            covered_tests = set(list(coverageData.cov_graph.neighbors(method)))
            failed_cov_test = covered_tests.intersection(set(coverageData.testResults.failed_tests))
            fw = float(sum([coverageData.cov_graph[method][f_test]["weight"] for f_test in failed_cov_test]))
            ef = len(covered_tests.intersection(set(coverageData.testResults.failed_tests)))
            ep = len(covered_tests.intersection(set(coverageData.testResults.passed_tests)))
            nf = len(coverageData.testResults.failed_tests) - ef

            tag1 = float(fw)
            tag2 = float(float(ef)+float(nf))*float(float(ef)+float(ep))
            if float(tag1)==0.0 or float(tag2)==0.0:
                self.score[method] = 0.0
            else:
                self.score[method] = float(tag1) / float(math.sqrt(float(tag2)))
        return self.score


    def set_jaccard(self, coverageData):
        methods = set(coverageData.methodNames).intersection(set(list(coverageData.cov_graph.nodes())))
        for method in methods:
            covered_tests = set(list(coverageData.cov_graph.neighbors(method)))
            ef = len(covered_tests.intersection(set(coverageData.testResults.failed_tests)))
            ep = len(covered_tests.intersection(set(coverageData.testResults.passed_tests)))
            nf = len(coverageData.testResults.failed_tests) - ef

            tag1 = float(ef)
            tag2 = float(ef)+float(nf)+float(ep)
            if float(tag1)==0.0 or float(tag2)==0.0:
                self.score[method] = 0.0
            else:
                self.score[method] = float(tag1) / float(tag2)
        return self.score


    def set_jaccard_2(self, coverageData):
        methods = set(coverageData.methodNames).intersection(set(list(coverageData.cov_graph.nodes())))
        for method in methods:
            covered_tests = set(list(coverageData.cov_graph.neighbors(method)))
            failed_cov_test = covered_tests.intersection(set(coverageData.testResults.failed_tests))
            fw = float(sum([coverageData.cov_graph[method][f_test]["weight"] for f_test in failed_cov_test]))
            ef = len(covered_tests.intersection(set(coverageData.testResults.failed_tests)))
            ep = len(covered_tests.intersection(set(coverageData.testResults.passed_tests)))
            nf = len(coverageData.testResults.failed_tests) - ef

            tag1 = float(fw)
            tag2 = float(ef)+float(nf)+float(ep)
            if float(tag1)==0.0 or float(tag2)==0.0:
                self.score[method] = 0.0
            else:
                self.score[method] = float(tag1) / float(tag2)
        return self.score



    def set_russell_rao(self, coverageData):
        methods = set(coverageData.methodNames).intersection(set(list(coverageData.cov_graph.nodes())))
        for method in methods:
            covered_tests = set(list(coverageData.cov_graph.neighbors(method)))
            ef = len(covered_tests.intersection(set(coverageData.testResults.failed_tests)))

            tag1 = float(ef)
            tag2 = len(coverageData.testResults.pass_failed_dict.keys())
            if float(tag1)==0.0 or float(tag2)==0.0:
                self.score[method] = 0.0
            else:
                self.score[method] = float(tag1) / float(tag2)
        return self.score


    def set_russell_rao_2(self, coverageData):
        methods = set(coverageData.methodNames).intersection(set(list(coverageData.cov_graph.nodes())))
        for method in methods:
            covered_tests = set(list(coverageData.cov_graph.neighbors(method)))
            failed_cov_test = covered_tests.intersection(set(coverageData.testResults.failed_tests))
            fw = float(sum([coverageData.cov_graph[method][f_test]["weight"] for f_test in failed_cov_test]))

            tag1 = float(fw)
            tag2 = len(coverageData.testResults.pass_failed_dict.keys())
            if float(tag1)==0.0 or float(tag2)==0.0:
                self.score[method] = 0.0
            else:
                self.score[method] = float(tag1) / float(tag2)
        return self.score





    def set_sorensen_dice(self, coverageData):
        methods = set(coverageData.methodNames).intersection(set(list(coverageData.cov_graph.nodes())))
        for method in methods:
            covered_tests = set(list(coverageData.cov_graph.neighbors(method)))
            ef = len(covered_tests.intersection(set(coverageData.testResults.failed_tests)))
            ep = len(covered_tests.intersection(set(coverageData.testResults.passed_tests)))
            nf = len(coverageData.testResults.failed_tests) - ef

            tag1 = float(ef)*2.0
            tag2 = 2.0*float(ef)+float(ep)+float(nf)
            if float(tag1)==0.0 or float(tag2)==0.0:
                self.score[method] = 0.0
            else:
                self.score[method] = float(tag1) / float(tag2)
        return self.score


    def set_sorensen_dice_2(self, coverageData):
        methods = set(coverageData.methodNames).intersection(set(list(coverageData.cov_graph.nodes())))
        for method in methods:
            covered_tests = set(list(coverageData.cov_graph.neighbors(method)))
            failed_cov_test = covered_tests.intersection(set(coverageData.testResults.failed_tests))
            fw = float(sum([coverageData.cov_graph[method][f_test]["weight"] for f_test in failed_cov_test]))
            ef = len(covered_tests.intersection(set(coverageData.testResults.failed_tests)))
            ep = len(covered_tests.intersection(set(coverageData.testResults.passed_tests)))
            nf = len(coverageData.testResults.failed_tests) - ef

            tag1 = float(fw)*2.0
            tag2 = 2.0*float(ef)+float(ep)+float(nf)
            if float(tag1)==0.0 or float(tag2)==0.0:
                self.score[method] = 0.0
            else:
                self.score[method] = float(tag1) / float(tag2)
        return self.score
