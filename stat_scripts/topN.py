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
    parser = argparse.ArgumentParser(description='calc. Top-N categories')
    parser.add_argument('-r', '--ranks', required=True, help='ranks csv')
    args = parser.parse_args()
    return args.ranks


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

algorithms = sorted(algorithms)

topN_dict = {"top-1": 1,
             "top-3": 3,
             "top-5": 5,
             "top-10": 10}



out_file = open("topN_count.csv", "w")
out_file.write(";Top-1;Top-3;Top-5;Top-10;other\n")
for algorithm in algorithms:
    out_str = str(algorithm)
    for topN, limit in topN_dict.items():
        _ = [x for x in all_data[algorithm] if x <= limit]
        out_str += ";"+str(len(_))
    _ = [x for x in all_data[algorithm] if x > 10.0]
    out_str += ";" + str(len(_))
    out_file.write(out_str+"\n")
out_file.close()


out_file = open("topN_percent.csv", "w")
out_file.write(";Top-1;Top-3;Top-5;Top-10;other\n")
for algorithm in algorithms:
    out_str = str(algorithm)
    for topN, limit in topN_dict.items():
        _ = [x for x in all_data[algorithm] if x <= limit]
        out_str += ";"+str(round(float(len(_))/float(len(all_data[algorithm]))*100,2)).replace(".", ",")
    _ = [x for x in all_data[algorithm] if x > 10.0]
    out_str += ";" + str(round(float(len(_)) / float(len(all_data[algorithm])) * 100, 2)).replace(".", ",")
    out_file.write(out_str+"\n")
out_file.close()


out_file = open("topN_mixed.csv", "w")
out_file.write(";Top-1 (%);Top-3(%);Top-5(%);Top-10(%);other(%)\n")
for algorithm in algorithms:
    out_str = str(algorithm)
    for topN, limit in topN_dict.items():
        _ = [x for x in all_data[algorithm] if x <= limit]
        out_str += ";"+str(len(_))+" ("+str(round(float(len(_))/float(len(all_data[algorithm]))*100,2)).replace(".", ",")+"%)"
    _ = [x for x in all_data[algorithm] if x > 10.0]
    out_str += ";" + str(len(_)) + " (" + str(round(float(len(_)) / float(len(all_data[algorithm])) * 100, 2)).replace(".", ",") + "%)"
    out_file.write(out_str+"\n")
out_file.close()