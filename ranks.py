import scipy.stats as ss
import scores


class RankContainer():
    def __init__(self, coverage, metrics):
        self.coverageData = coverage
        self.rank_dict = {}
        self.metrics = metrics


    def add_ranks(self):
        for metric in self.metrics:
            self._add_ranks(metric)


    def _add_ranks(self, metricName):
        rank = Rank(metricName, self.coverageData)
        self.rank_dict[metricName]=rank.get_rank()


    def printMinRanks(self, bugID):
        header = self.get_header()
        bugrank_list = list()
        for h in header:
            bugrank_list.append(str(min(self.get_fixed_rank_list(str(h)))).replace(".", ","))
        print(str(bugID)+";"+";".join(bugrank_list))


    def get_fixed_rank_list(self, metricName):
        fix_ranks = list()
        for fix in self.coverageData.fixed_methods:
            if fix in self.rank_dict[metricName]:
                fix_ranks.append( self.rank_dict[metricName][fix] )
        if len(fix_ranks)==0:
            fix_ranks.append(99999999999)
        return fix_ranks


    def get_header(self):
        header = list()
        for m in self.metrics:
            header.append(str(m))
        return header


class Rank():
    def __init__(self, metricName, coverageData):
        self.score = scores.Score(metricName, coverageData)
        self.rank = {}

    def get_rank(self):
        item_vector=[]
        res_vector=[]
        score_res = sorted(self.score.score, key=self.score.score.__getitem__, reverse=True)
        for item in score_res:
            item_vector.append(item)
            res_vector.append( abs(max(self.score.score.values()) - self.score.score[item]))
        rank_vektor = ss.rankdata(res_vector, method='average')

        rank_dict = {}
        for x in range(len(item_vector)):
            rank_dict[item_vector[x]] = rank_vektor[x]
        return rank_dict


