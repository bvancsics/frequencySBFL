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
    parser = argparse.ArgumentParser(description='calc Top-N interval categories')
    parser.add_argument('-r', '--ranks', required=True, help='ranks csv')
    args = parser.parse_args()
    return args.ranks


ranks_csv = arg_parser()
f = open(ranks_csv, 'r')
reader = csv.reader(f, delimiter=";")
algorithms = list(next(reader, None))[2:]


import networkx as nx
tops = ["[1]", "(1,3]", "(3,5]", "(5,10]", "other"]
results_graph = nx.DiGraph()
for algorithm in algorithms:
    for top in tops:
        results_graph.add_node(str(algorithm)+" X "+str(top))








data = {}
all_data = {}
for algorithm in algorithms:
    all_data[algorithm] = list()


def topN_calc(rank):
    if rank==1.0:
        return "[1]"
    elif rank <= 3.0:
        return "(1,3]"
    elif rank <= 5.0:
        return "(3,5]"
    elif rank <= 10.0:
        return "(5,10]"
    else:
        return "other"

def edge_calc(alg_1, alg_2, algorithms, rank_1, rank_2, results_graph):
    algorithm1 = algorithms[alg_1]
    algorithm2 = algorithms[alg_2]
    rank_1_cat = topN_calc(rank_1)
    rank_2_cat = topN_calc(rank_2)
    node_1 = str(algorithm1) + " X " + str(rank_1_cat)
    node_2 = str(algorithm2) + " X " + str(rank_2_cat)
    if not results_graph.has_edge(node_1, node_2):
        results_graph.add_edge(node_1, node_2)
        results_graph[node_1][node_2]["weight"] = 0
    results_graph[node_1][node_2]["weight"] += 1
    return results_graph


try:
    while True:
        results = next(reader)
        project = results[0]
        if project not in data:
            data[project] = {}
            for algorithm in algorithms:
                data[project][algorithm] = list()

        ranks_list = list([float(str(x).replace(",", ".")) for x in results[2:]])

        for alg_1 in range(len(algorithms)):
            for alg_2 in range(len(algorithms)):
                results_graph = edge_calc(alg_1, alg_2, algorithms, ranks_list[alg_1], ranks_list[alg_2], results_graph)

except StopIteration:
    pass


output_file = open("topN_interval_move.csv", "w")
for alg_1_index in range(len(algorithms)-1):
    for alg_2_index in range(alg_1_index, len(algorithms)):
        if alg_1_index != alg_2_index:
            alg_1 = algorithms[alg_1_index]
            alg_2 = algorithms[alg_2_index]
            output_file.write(str(alg_1)+"->"+str(alg_2)+";"+";".join(tops)+"\n")
            for top1 in tops:
                out_str = str(top1)
                node_1 = str(alg_1)+" X "+str(top1)
                for top2 in tops:
                    node_2 = str(alg_2) + " X " + str(top2)
                    weight = 0
                    if results_graph.has_edge(node_1, node_2):
                        weight = results_graph[node_1][node_2]["weight"]
                    out_str += str(";")+str(weight)
                output_file.write(out_str+"\n")
            output_file.write("\n")
output_file.close()