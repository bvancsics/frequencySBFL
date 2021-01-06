from __future__ import division
from scipy import stats
import argparse
import csv

"""
input (file) format:
project;bugID;ALG;ALG-2;...
time;1;RANK;RANK;...
time;2;RANK;RANK;...
...
lang;1;RANK;RANK;...
...
"""


def arg_parser():
    parser = argparse.ArgumentParser(description='calc. Wilcoxon test')
    parser.add_argument('-r', '--ranks', required=True, help='ranks csv')
    args = parser.parse_args()
    return args.ranks



def cliffsDelta(lst1, lst2, **dull):

    """Returns delta and true if there are more than 'dull' differences"""
    if not dull:
        dull = {'small': 0.147, 'medium': 0.33, 'large': 0.474} # effect sizes from (Hess and Kromrey, 2004)
    m, n = len(lst1), len(lst2)
    lst2 = sorted(lst2)
    j = more = less = 0
    for repeats, x in runs(sorted(lst1)):
        while j <= (n - 1) and lst2[j] < x:
            j += 1
        more += j*repeats
        while j <= (n - 1) and lst2[j] == x:
            j += 1
        less += (n - j)*repeats
    d = (more - less) / (m*n)
    size = lookup_size(d, dull)
    return d, size


def lookup_size(delta: float, dull: dict) -> str:
    """
    :type delta: float
    :type dull: dict, a dictionary of small, medium, large thresholds.
    """
    delta = abs(delta)
    if delta < dull['small']:
        return 'negligible'
    if dull['small'] <= delta < dull['medium']:
        return 'small'
    if dull['medium'] <= delta < dull['large']:
        return 'medium'
    if delta >= dull['large']:
        return 'large'


def runs(lst):
    """Iterator, chunks repeated values"""
    for j, two in enumerate(lst):
        if j == 0:
            one, i = two, 0
        if one != two:
            yield j - i, one
            i = j
        one = two
    yield j - i + 1, two




ranks_csv = arg_parser()
f = open(ranks_csv, 'r')
reader = csv.reader(f, delimiter=";")
algorithms = list(next(reader, None))[2:]

data = {}
all_data = {}
for algorithm in algorithms:
    all_data[algorithm] = list()

try:
    while True:
        results = next(reader)
        project = results[0]
        if project not in data:
            data[project] = {}
            for algorithm in algorithms:
                data[project][algorithm] = list()

        ranks_list = list(results[2:])
        for index in range(len(ranks_list)):
            data[project][algorithms[index]].append(float(str(ranks_list[index]).replace(",",".")))
            all_data[algorithms[index]].append(float(str(ranks_list[index]).replace(",",".")))

except StopIteration:
    pass



topN_dict = {"top-1": 1.0,
             "top-3": 3.0,
             "top-5": 5.0,
             "top-10": 10.0}


output_file = open("wilcoxon_TopN.csv", "w")
output_file.write("project;top-N;base algorithm;algorithm;p-value (Wilcoxon, zsplit);p-value (Wilcoxon, pratt);p-value (Wilcoxon, wilcox);d(Cliff);magn.(Cliff)\n")
for topN, limit in topN_dict.items():
    for project in data.keys():
        for alg1_index in range(len(algorithms)):
            algorithm1 = algorithms[alg1_index]
            for alg2_index in range(len(algorithms)):
                algorithm2 = algorithms[alg2_index]
                if algorithm1 != algorithm2:
                    base_IDs = list([rank_index for rank_index in range(len(data[project][algorithm1])) if float(str(data[project][algorithm1][rank_index]).replace(",", ".")) <= float(limit)])
                    data_alg1 = list([data[project][algorithm1][index] for index in base_IDs])
                    data_alg2 = list([data[project][algorithm2][index] for index in base_IDs])

                    _, pW1 = stats.wilcoxon(data_alg1, data_alg2, zero_method='zsplit')
                    _, pW2 = stats.wilcoxon(data_alg1, data_alg2, zero_method='pratt')
                    _, pW3 = stats.wilcoxon(data_alg1, data_alg2, zero_method='wilcox')

                    try:
                        d, size = cliffsDelta(data_alg1, data_alg2)
                        output_file.write(str(project)+";"+
                                          str(topN) + ";" +
                                          str(algorithm1) + ";" +
                                          str(algorithm2) + ";" +
                                          str(round(float(pW1), 4)).replace(".", ",")+";"+
                                          str(round(float(pW2), 4)).replace(".", ",") + ";" +
                                          str(round(float(pW3), 4)).replace(".", ",") + ";" +
                                          str(round(float(d), 4)).replace(".", ",")+";"+
                                          str(size)+"\n")

                    except:
                        pass


for project in data.keys():
    for alg1_index in range(len(algorithms)):
        algorithm1 = algorithms[alg1_index]
        for alg2_index in range(len(algorithms)):
            algorithm2 = algorithms[alg2_index]
            if algorithm1 != algorithm2:
                base_IDs = list([rank_index for rank_index in range(len(data[project][algorithm1])) if float(str(data[project][algorithm1][rank_index]).replace(",", ".")) > 10.0])
                data_alg1 = list([data[project][algorithm1][index] for index in base_IDs])
                data_alg2 = list([data[project][algorithm2][index] for index in base_IDs])

                _, pW1 = stats.wilcoxon(data_alg1, data_alg2, zero_method='zsplit')
                _, pW2 = stats.wilcoxon(data_alg1, data_alg2, zero_method='pratt')
                _, pW3 = stats.wilcoxon(data_alg1, data_alg2, zero_method='wilcox')

                try:
                    d, size = cliffsDelta(data_alg1, data_alg2)
                    output_file.write(str(project)+";"+
                                      str("other") + ";" +
                                      str(algorithm1) + ";" +
                                      str(algorithm2) + ";" +
                                      str(round(float(pW1), 4)).replace(".", ",")+";"+
                                      str(round(float(pW2), 4)).replace(".", ",") + ";" +
                                      str(round(float(pW3), 4)).replace(".", ",") + ";" +
                                      str(round(float(d), 4)).replace(".", ",")+";"+
                                      str(size)+"\n")

                except:
                    pass






















for topN, limit in topN_dict.items():
    for alg1_index in range(len(algorithms)):
        algorithm1 = algorithms[alg1_index]
        for alg2_index in range(len(algorithms)):
            algorithm2 = algorithms[alg2_index]
            if algorithm1 != algorithm2:
                #try:
                base_IDs = list([rank_index for rank_index in range(len(all_data[algorithm1])) if float(str(all_data[algorithm1][rank_index]).replace(",", ".")) <= float(limit)])
                data_alg1 = list([all_data[algorithm1][index] for index in base_IDs])
                data_alg2 = list([all_data[algorithm2][index] for index in base_IDs])

                _, pW1 = stats.wilcoxon(data_alg1, data_alg2, zero_method='zsplit')
                _, pW2 = stats.wilcoxon(data_alg1, data_alg2, zero_method='pratt')
                _, pW3 = stats.wilcoxon(data_alg1, data_alg2, zero_method='wilcox')

                try:
                    d, size = cliffsDelta(data_alg1, data_alg2)
                    output_file.write("all;"+
                                      str(topN) + ";" +
                                      str(algorithm1) + ";" +
                                      str(algorithm2) + ";" +
                                      str(round(float(pW1), 4)).replace(".", ",")+";"+
                                      str(round(float(pW2), 4)).replace(".", ",") + ";" +
                                      str(round(float(pW3), 4)).replace(".", ",") + ";" +
                                      str(round(float(d), 4)).replace(".", ",")+";"+
                                      str(size)+"\n")

                except:
                    pass


for alg1_index in range(len(algorithms)):
    algorithm1 = algorithms[alg1_index]
    for alg2_index in range(len(algorithms)):
        algorithm2 = algorithms[alg2_index]
        if algorithm1 != algorithm2:
            base_IDs = list([rank_index for rank_index in range(len(all_data[algorithm1])) if float(str(all_data[algorithm1][rank_index]).replace(",", ".")) > 10.0])
            data_alg1 = list([all_data[algorithm1][index] for index in base_IDs])
            data_alg2 = list([all_data[algorithm2][index] for index in base_IDs])
            _, pW1 = stats.wilcoxon(data_alg1, data_alg2, zero_method='zsplit')
            _, pW2 = stats.wilcoxon(data_alg1, data_alg2, zero_method='pratt')
            _, pW3 = stats.wilcoxon(data_alg1, data_alg2, zero_method='wilcox')

            try:
                d, size = cliffsDelta(data_alg1, data_alg2)
                output_file.write("all;"+
                                  str("other") + ";" +
                                  str(algorithm1) + ";" +
                                  str(algorithm2) + ";" +
                                  str(round(float(pW1), 4)).replace(".", ",")+";"+
                                  str(round(float(pW2), 4)).replace(".", ",") + ";" +
                                  str(round(float(pW3), 4)).replace(".", ",") + ";" +
                                  str(round(float(d), 4)).replace(".", ",")+";"+
                                  str(size)+"\n")

            except:
                pass