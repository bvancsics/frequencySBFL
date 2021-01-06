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
    parser = argparse.ArgumentParser(description='calc average ranks')
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

out_file = open("average_ranks.csv", "w")
out_file.write("project;"+";".join(algorithms)+"\n")
for project in data.keys():
    out_str = str(project)
    for algorithm in algorithms:
        avg = float(sum(data[project][algorithm]))/float(len(data[project][algorithm]))
        out_str += ";"+str(round(avg,2)).replace(".", ",")
    out_file.write(out_str+"\n")


out_str = str("all")
for algorithm in algorithms:
    avg = float(sum(all_data[algorithm]))/float(len(all_data[algorithm]))
    out_str += ";"+str(round(avg,2)).replace(".", ",")
out_file.write(out_str+"\n")

out_file.close()