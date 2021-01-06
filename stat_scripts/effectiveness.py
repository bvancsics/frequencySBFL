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
    parser = argparse.ArgumentParser(description='calc. effectiveness')
    parser.add_argument('-r', '--ranks', required=True, help='ranks csv ')
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


functions = {"lang": 2200,
             "time": 4200,
             "chart": 10300,
             "math": 5200,
             "mockito": 1300,
             "closure": 9600,
             "all": 5500}


algorithms = sorted(algorithms)
hit_alg = [algorithm for algorithm in algorithms if str(algorithm).count("-C")== 0]

pairs = set()
for algorithm in hit_alg:
    pairs.add( (algorithm, str(algorithm)+"-C"))

projects = list(data.keys())
out_file = open("effectiveness.csv","w")
out_file.write(";"+";".join(projects)+";all\n")


for pair in pairs:
    algorithm1 = pair[0]
    algorithm2 = pair[1]

    out_str = str(algorithm1) + "-E (E')"
    for project in projects:
        e_1 = round(float(sum(data[project][algorithm1])) / float(len(data[project][algorithm1])),1)
        e2_1 = round(e_1 / float(functions[project]) * 100.0, 2)
        out_str += ";" + str(e_1).replace(".", ",") + " (" + str(e2_1).replace(".", ",") + "%)"
    e_1 = round(float(sum(all_data[algorithm1])) / float(len(all_data[algorithm1])),1)
    e2_1 = round(e_1 / float(functions["all"]) * 100.0, 2)
    out_str += ";" + str(e_1).replace(".", ",") + " (" + str(e2_1).replace(".", ",") + "%)"
    out_file.write(out_str+"\n")


    out_str = str(algorithm2) + "-E (E')"
    for project in projects:
        e_2 = round(float(sum(data[project][algorithm2]))/float(len(data[project][algorithm2])),1)
        e2_2 = round(e_2 / float(functions[project])*100.0, 2)
        out_str += ";" + str(e_2).replace(".", ",") + " (" + str(e2_2).replace(".", ",") + "%)"
    e_2 = round(float(sum(all_data[algorithm2]))/float(len(all_data[algorithm2])),1)
    e2_2 = round(e_2 / float(functions["all"])*100.0, 2)
    out_str += ";" + str(e_2).replace(".", ",") + " (" + str(e2_2).replace(".", ",") + "%)"
    out_file.write(out_str + "\n")


    out_str = "diff E (E')"
    for project in projects:
        e_1 = round(float(sum(data[project][algorithm1])) / float(len(data[project][algorithm1])),1)
        e2_1 = round(e_1 / float(functions[project]) * 100.0, 2)
        e_2 = round(float(sum(data[project][algorithm2]))/float(len(data[project][algorithm2])),1)
        e2_2 = round(e_2 / float(functions[project])*100.0, 2)
        out_str += ";" + str(round(e_2-e_1,1)).replace(".", ",")+ " (" + str(round(e2_2-e2_1, 2)).replace(".", ",")+"%)"
    e_1 = round(float(sum(all_data[algorithm1])) / float(len(all_data[algorithm1])),1)
    e2_1 = round(e_1 / float(functions["all"]) * 100.0, 2)
    e_2 = round(float(sum(all_data[algorithm2]))/float(len(all_data[algorithm2])),1)
    e2_2 = round(e_2 / float(functions["all"])*100.0, 2)
    out_str += ";" + str(round(e_2-e_1,1)).replace(".", ",")+ " (" + str(round(e2_2-e2_1, 2)).replace(".", ",")+"%)"
    out_file.write(out_str + "\n")

    out_str = "relative change (%)"
    for project in projects:
        e_1 = round(float(sum(data[project][algorithm1])) / float(len(data[project][algorithm1])),1)
        e2_1 = round(e_1 / float(functions[project]) * 100.0, 2)
        e_2 = round(float(sum(data[project][algorithm2]))/float(len(data[project][algorithm2])),1)
        e2_2 = round(e_2 / float(functions[project])*100.0, 2)
        out_str += ";" + str(int(round(float(e_2-e_1)/float(e_1)*100.0,0))).replace(".", ",")

    e_1 = round(float(sum(all_data[algorithm1])) / float(len(all_data[algorithm1])),1)
    e2_1 = round(e_1 / float(functions["all"]) * 100.0, 2)
    e_2 = round(float(sum(all_data[algorithm2]))/float(len(all_data[algorithm2])),1)
    e2_2 = round(e_2 / float(functions["all"])*100.0, 2)
    out_str += ";" + str(int(round(float(e_2 - e_1) / float(e_1) * 100.0, 0))).replace(".", ",")
    out_file.write(out_str+"\n")

