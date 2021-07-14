

class Score():
    def __init__(self, metricName, coverageData):
        self.metricName = metricName
        self.score = self.set_score(metricName, coverageData)

    def set_score(self, metricName, coverageData):
        if str(metricName).startswith("Barinel"):
            return self.barinel(coverageData, metricName)
        elif str(metricName).startswith("DStar"):
            return self.dstar(coverageData, metricName)
        elif str(metricName).startswith("GP13"):
            return self.gp13(coverageData, metricName)
        elif str(metricName).startswith("Jaccard"):
            return self.jaccard(coverageData, metricName)
        elif str(metricName).startswith("Naish2"):
            return self.naish2(coverageData, metricName)
        elif str(metricName).startswith("Ochiai"):
            return self.ochiai(coverageData, metricName)
        elif str(metricName).startswith("RusselRao"):
            return self.russel_rao(coverageData, metricName)
        elif str(metricName).startswith("SorensenDice"):
            return self.sorensen_dice(coverageData, metricName)
        elif str(metricName).startswith("Tarantula"):
            return self.tarantula(coverageData, metricName)

    def barinel(self, coverageData, metricName):
        import algorithms.SBFL.Barinel as SBFL_Barinel
        return SBFL_Barinel.Barinel().call(metricName,
                                           coverageData.methodNames,
                                           coverageData.fourMetrics.hit_results.results,
                                           coverageData.fourMetrics.unique_results.results,
                                           coverageData.fourMetrics.naive_results.results)

    def dstar(self, coverageData, metricName):
        import algorithms.SBFL.Dstar as SBFL_DStar
        return SBFL_DStar.DStar().call(metricName,
                                       coverageData.methodNames,
                                       coverageData.fourMetrics.hit_results.results,
                                       coverageData.fourMetrics.unique_results.results,
                                       coverageData.fourMetrics.naive_results.results)

    def gp13(self, coverageData, metricName):
        import algorithms.SBFL.GP13 as SBFL_GP13
        return SBFL_GP13.GP13().call(metricName,
                                     coverageData.methodNames,
                                     coverageData.fourMetrics.hit_results.results,
                                     coverageData.fourMetrics.unique_results.results,
                                     coverageData.fourMetrics.naive_results.results)

    def jaccard(self, coverageData, metricName):
        import algorithms.SBFL.Jaccard as SBFL_Jaccard
        return SBFL_Jaccard.Jaccard().call(metricName,
                                           coverageData.methodNames,
                                           coverageData.fourMetrics.hit_results.results,
                                           coverageData.fourMetrics.unique_results.results,
                                           coverageData.fourMetrics.naive_results.results)

    def naish2(self, coverageData, metricName):
        import algorithms.SBFL.Naish2 as SBFL_Naish2
        return SBFL_Naish2.Naish2().call(metricName,
                                         coverageData.methodNames,
                                         coverageData.fourMetrics.hit_results.results,
                                         coverageData.fourMetrics.unique_results.results,
                                         coverageData.fourMetrics.naive_results.results)


    def ochiai(self, coverageData, metricName):
        import algorithms.SBFL.Ochiai as SBFL_Ochiai
        return SBFL_Ochiai.Ochiai().call(metricName,
                                         coverageData.methodNames,
                                         coverageData.fourMetrics.hit_results.results,
                                         coverageData.fourMetrics.unique_results.results,
                                         coverageData.fourMetrics.naive_results.results)

    def russel_rao(self, coverageData, metricName):
        import algorithms.SBFL.RusselRao as SBFL_RusselRao
        return SBFL_RusselRao.RusselRao().call(metricName,
                                               coverageData.methodNames,
                                               coverageData.fourMetrics.hit_results.results,
                                               coverageData.fourMetrics.unique_results.results,
                                               coverageData.fourMetrics.naive_results.results)

    def sorensen_dice(self, coverageData, metricName):
        import algorithms.SBFL.SorensenDice as SBFL_SorensenDice
        return SBFL_SorensenDice.SorensenDice().call(metricName,
                                                     coverageData.methodNames,
                                                     coverageData.fourMetrics.hit_results.results,
                                                     coverageData.fourMetrics.unique_results.results,
                                                     coverageData.fourMetrics.naive_results.results)

    def tarantula(self, coverageData, metricName):
        import algorithms.SBFL.Tarantula as SBFL_Tarantula
        return SBFL_Tarantula.Tarantula().call(metricName,
                                               coverageData.methodNames,
                                               coverageData.fourMetrics.hit_results.results,
                                               coverageData.fourMetrics.unique_results.results,
                                               coverageData.fourMetrics.naive_results.results)