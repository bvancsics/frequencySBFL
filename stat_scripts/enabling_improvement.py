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
    parser = argparse.ArgumentParser(description='calc. enabling improvements')
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





projects = data.keys()
out_file = open("enabling_improvement.csv", "w")

for algorithm1 in algorithms:
    for algorithm2 in algorithms:
        if algorithm1 != algorithm2:
            out_file.write(str(algorithm1)+" vs "+str(algorithm2)+";"+str(algorithm1)+" > 10 (%);enabling imp. (%);relative impr. (%)\n")
            for project in projects:
                nagyobb_10 = 0
                enable_imp = 0
                diffs = 0.0
                avg_old_rank = 0.0
                for index in range(len(data[project][algorithm1])):
                    old_rank = data[project][algorithm1][index]
                    fwe_rank = data[project][algorithm2][index]
                    if old_rank > 10.0:
                        nagyobb_10 += 1
                        if fwe_rank <= 10.0:
                            enable_imp += 1
                            diffs += (fwe_rank - old_rank)
                            avg_old_rank += old_rank

                try:
                    avg_diff = float(diffs) / float(enable_imp)
                    avg_old_rank = float(avg_old_rank) / float(enable_imp)
                    out_file.write(str(project) + ";" +
                                   str(nagyobb_10) + " (" +
                                   str(round(float(nagyobb_10) / float(len(data[project][algorithm1])) * 100.0,
                                             0)) + "%);" +
                                   str(enable_imp) + " (" +
                                   str(round(float(enable_imp) / float(len(data[project][algorithm2])) * 100.0,
                                             0)) + "%);" +
                                   str(round(avg_diff, 1)) + " (" +
                                   str(round(float(avg_diff) / float(avg_old_rank) * 100.0, 0)) + "%)\n"
                                   )
                except:
                    pass

            nagyobb_10 = 0
            enable_imp = 0
            diffs = 0.0
            avg_old_rank = 0.0
            for project in projects:
                for index in range(len(data[project][algorithm1])):
                    old_rank = data[project][algorithm1][index]
                    fwe_rank = data[project][algorithm2][index]
                    if old_rank > 10.0:
                        nagyobb_10 += 1
                        if fwe_rank <= 10.0:
                            enable_imp += 1
                            diffs += (fwe_rank - old_rank)
                            avg_old_rank += old_rank

            num_of_bugs = len(all_data[algorithm1])

            try:
                avg_diff = float(diffs) / float(enable_imp)
                avg_old_rank = float(avg_old_rank) / float(enable_imp)
                out_file.write(str("all") + ";" +
                               str(nagyobb_10) + " (" +
                               str(round(float(nagyobb_10) / float(num_of_bugs) * 100.0, 0)) + "%);" +
                               str(enable_imp) + " (" +
                               str(round(float(enable_imp) / float(num_of_bugs) * 100.0, 0)) + "%);" +
                               str(round(avg_diff, 1)) + " (" +
                               str(round(float(avg_diff) / float(avg_old_rank) * 100.0, 0)) + "%)\n"
                               )
            except ZeroDivisionError:
                out_file.write(str("all") + ";" +
                               str(nagyobb_10) + " (" +
                               str(round(float(nagyobb_10) / float(num_of_bugs) * 100.0, 0)) + "%);" +
                               str(0) + " (" +
                               str(0) + "%);" +
                               str(0) + " (" +
                               str(0) + "%)\n"
                               )

            out_file.write("\n\n")
