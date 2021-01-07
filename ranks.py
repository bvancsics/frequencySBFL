import collections
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
        my_d = collections.defaultdict(list)
        for key, val in self.score.score.items():
            my_d[max(self.score.score.values()) - val].append(key)

        ranked_key_list = []
        n = v = 1
        for _, my_list in sorted(my_d.items()):
            v = n + (len(my_list)-1)/2
            for e in my_list:
                n += 1
                ranked_key_list.append((e, v))

        rank_dict = {}
        for (method, rank) in ranked_key_list:
            rank_dict[method] = rank
        return rank_dict


