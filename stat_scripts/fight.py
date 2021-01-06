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
    parser = argparse.ArgumentParser(description='ide jon valami')
    parser.add_argument('-r', '--ranks', required=True, help='ranks csv')
    args = parser.parse_args()
    return args.ranks


ranks_csv = arg_parser()
f = open(ranks_csv, 'r')
reader = csv.reader(f, delimiter=";")
algorithms = list(next(reader, None))[2:]

all_data = {}
for algorithm in algorithms:
    all_data[algorithm] = list()

try:
    while True:
        results = next(reader)
        ranks_list = list(results[2:])
        for index in range(len(ranks_list)):
            all_data[algorithms[index]].append(float(str(ranks_list[index]).replace(",",".")))
except StopIteration:
    pass


number_of_bugs = len(all_data[algorithms[0]])

algorithms = sorted(algorithms)
hit_alg = [algorithm for algorithm in algorithms if str(algorithm).count("-C")== 0]

output_file = open("fight_percent.csv", "w")
output_file.write(";"+";".join(hit_alg)+"\n")


out_str = "a < b"
for alg_1 in range(len(hit_alg)):
    if str(hit_alg[alg_1]).count("-C") == 0:
        algorithm1 = hit_alg[alg_1]
        algorithm2 = str(hit_alg[alg_1])+"-C"
        data1 = all_data[algorithm1]
        data2 = all_data[algorithm2]
        win = round(float(sum([1 for index in range(len(data1)) if data1[index] < data2[index]])) / float(number_of_bugs) * 100.0, 1)
        out_str = str(out_str) + ";" + str(win).replace(".", ",")
output_file.write(out_str+"\n")



out_str = "a = b"
for alg_1 in range(len(hit_alg)):
    if str(hit_alg[alg_1]).count("-C") == 0:
        algorithm1 = hit_alg[alg_1]
        algorithm2 = str(hit_alg[alg_1])+"-C"
        data1 = all_data[algorithm1]
        data2 = all_data[algorithm2]
        draw = round(float(sum([1 for index in range(len(data1)) if data1[index] == data2[index]])) / float(number_of_bugs) * 100.0, 1)
        out_str = str(out_str) + ";" + str(draw).replace(".", ",")
output_file.write(out_str+"\n")



out_str = "a > b"
for alg_1 in range(len(hit_alg)):
    if str(hit_alg[alg_1]).count("-C") == 0:
        algorithm1 = hit_alg[alg_1]
        algorithm2 = str(hit_alg[alg_1])+"-C"
        data1 = all_data[algorithm1]
        data2 = all_data[algorithm2]
        defeat = round(float(sum([1 for index in range(len(data1)) if data1[index] > data2[index]])) / float(number_of_bugs) * 100.0, 1)
        out_str = str(out_str) + ";" + str(defeat).replace(".", ",")
output_file.write(out_str+"\n")


out_str = "a <= b"
for alg_1 in range(len(hit_alg)):
    if str(hit_alg[alg_1]).count("-C") == 0:
        algorithm1 = hit_alg[alg_1]
        algorithm2 = str(hit_alg[alg_1])+"-C"
        data1 = all_data[algorithm1]
        data2 = all_data[algorithm2]
        not_defeat = round(float(sum([1 for index in range(len(data1)) if data1[index] <= data2[index]])) / float(number_of_bugs) * 100.0, 1)
        out_str = str(out_str) + ";" + str(not_defeat).replace(".", ",")
output_file.write(out_str+"\n")
output_file.close()

# ***************************************************************************************
# ***************************************************************************************

output_file2 = open("fight_count.csv", "w")
output_file2.write(";"+";".join([algorithm for algorithm in algorithms if str(algorithm).count("-C")== 0])+"\n")
out_str = "a < b"
for alg_1 in range(len(hit_alg)):
    if str(hit_alg[alg_1]).count("-C") == 0:
        algorithm1 = hit_alg[alg_1]
        algorithm2 = str(hit_alg[alg_1])+"-C"
        data1 = all_data[algorithm1]
        data2 = all_data[algorithm2]
        win = sum([1 for index in range(len(data1)) if data1[index] < data2[index]])
        out_str = str(out_str) + ";" + str(win).replace(".", ",")
output_file2.write(out_str+"\n")



out_str = "a = b"
for alg_1 in range(len(hit_alg)):
    if str(hit_alg[alg_1]).count("-C") == 0:
        algorithm1 = hit_alg[alg_1]
        algorithm2 = str(hit_alg[alg_1])+"-C"
        data1 = all_data[algorithm1]
        data2 = all_data[algorithm2]
        draw = sum([1 for index in range(len(data1)) if data1[index] == data2[index]])
        out_str = str(out_str) + ";" + str(draw).replace(".", ",")
output_file2.write(out_str+"\n")



out_str = "a > b"
for alg_1 in range(len(hit_alg)):
    if str(hit_alg[alg_1]).count("-C") == 0:
        algorithm1 = hit_alg[alg_1]
        algorithm2 = str(hit_alg[alg_1])+"-C"
        data1 = all_data[algorithm1]
        data2 = all_data[algorithm2]
        defeat = sum([1 for index in range(len(data1)) if data1[index] > data2[index]])
        out_str = str(out_str) + ";" + str(defeat).replace(".", ",")
output_file2.write(out_str+"\n")


out_str = "a <= b"
for alg_1 in range(len(hit_alg)):
    if str(hit_alg[alg_1]).count("-C") == 0:
        algorithm1 = hit_alg[alg_1]
        algorithm2 = str(hit_alg[alg_1])+"-C"
        data1 = all_data[algorithm1]
        data2 = all_data[algorithm2]
        not_defeat = sum([1 for index in range(len(data1)) if data1[index] <= data2[index]])
        out_str = str(out_str) + ";" + str(not_defeat).replace(".", ",")
output_file2.write(out_str+"\n")
output_file2.close()


# ****************************************************************************
# ****************************************************************************


output_file3 = open("fight_mixed.csv", "w")
output_file3.write(";"+";".join(hit_alg)+"\n")


out_str = "a < b"
for alg_1 in range(len(hit_alg)):
    if str(hit_alg[alg_1]).count("-C") == 0:
        algorithm1 = hit_alg[alg_1]
        algorithm2 = str(hit_alg[alg_1])+"-C"
        data1 = all_data[algorithm1]
        data2 = all_data[algorithm2]
        win = round(float(sum([1 for index in range(len(data1)) if data1[index] < data2[index]])) / float(number_of_bugs) * 100.0, 1)
        win_c = sum([1 for index in range(len(data1)) if data1[index] < data2[index]])
        out_str = str(out_str) + ";" + str(win_c).replace(".", ",")+" ("+str(win)+"%)"
output_file3.write(out_str+"\n")



out_str = "a = b"
for alg_1 in range(len(hit_alg)):
    if str(hit_alg[alg_1]).count("-C") == 0:
        algorithm1 = hit_alg[alg_1]
        algorithm2 = str(hit_alg[alg_1])+"-C"
        data1 = all_data[algorithm1]
        data2 = all_data[algorithm2]
        draw = round(float(sum([1 for index in range(len(data1)) if data1[index] == data2[index]])) / float(number_of_bugs) * 100.0, 1)
        draw_c = sum([1 for index in range(len(data1)) if data1[index] == data2[index]])
        out_str = str(out_str) + ";" + str(draw_c).replace(".", ",")+" ("+str(draw)+"%)"
output_file3.write(out_str+"\n")



out_str = "a > b"
for alg_1 in range(len(hit_alg)):
    if str(hit_alg[alg_1]).count("-C") == 0:
        algorithm1 = hit_alg[alg_1]
        algorithm2 = str(hit_alg[alg_1])+"-C"
        data1 = all_data[algorithm1]
        data2 = all_data[algorithm2]
        defeat = round(float(sum([1 for index in range(len(data1)) if data1[index] > data2[index]])) / float(number_of_bugs) * 100.0, 1)
        defeat_c = sum([1 for index in range(len(data1)) if data1[index] > data2[index]])
        out_str = str(out_str) + ";" + str(defeat_c).replace(".", ",")+" ("+str(defeat)+"%)"
output_file3.write(out_str+"\n")


out_str = "a <= b"
for alg_1 in range(len(hit_alg)):
    if str(hit_alg[alg_1]).count("-C") == 0:
        algorithm1 = hit_alg[alg_1]
        algorithm2 = str(hit_alg[alg_1])+"-C"
        data1 = all_data[algorithm1]
        data2 = all_data[algorithm2]
        not_defeat = round(float(sum([1 for index in range(len(data1)) if data1[index] <= data2[index]])) / float(number_of_bugs) * 100.0, 1)
        not_defeat_c = sum([1 for index in range(len(data1)) if data1[index] <= data2[index]])
        out_str = str(out_str) + ";" + str(not_defeat_c).replace(".", ",")+" ("+str(not_defeat)+"%)"
output_file3.write(out_str+"\n")
output_file3.close()