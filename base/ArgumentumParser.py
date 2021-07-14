import argparse

def arg_parser():
    parser = argparse.ArgumentParser(description = 'ide jon valami')
    parser.add_argument('-nf', '--naive-folder', help='naive coverage folder')
    parser.add_argument('-ff', '--unique-folder', help='unique coverage folder ')
    parser.add_argument('-nm', '--naive-mapper', help='naive id - method-names pairs')
    parser.add_argument('-fm', '--unique-mapper', help='unique id - method-names pairs')
    parser.add_argument('-x', '--change', required=True, help='changes file')
    parser.add_argument('-b', '--bugID', required=True, help='defects4j bugID')
    parser.add_argument('-r', '--rank-method', choices=['average', 'min', 'max'])

    param_dict = {}
    args = parser.parse_args()
    param_dict["naive-folder"] = args.naive_folder or None
    param_dict["unique-folder"] = args.unique_folder or None
    param_dict["naive-mapper"] = args.naive_mapper or None
    param_dict["unique-mapper"] = args.unique_mapper or None
    param_dict["rank-method"] = "average" if args.rank_method is None else args.rank_method
    param_dict["change"] = args.change
    param_dict["bugID"] = args.bugID
    return param_dict


def get_metrics():
    metrics = list()
    formulas = ['Barinel', 'DStar', 'GP13', 'Jaccard', 'Naish2', 'Ochiai', 'RusselRao', 'SorensenDice', 'Tarantula']
    concepts = ["naive", "unique"]
    replaces = ["num_ef", "ef", "ef_ep", "ef_ep_nf_np"]

    for formula in formulas:
        metrics.append(formula+"-hit")
        for concept in concepts:
            for replace in replaces:
                metrics.append(formula+"-"+concept+"-"+replace)

            if formula in ['GP13', 'Naish2', 'Tarantula']:
                metrics.remove(formula+"-"+concept+"-num_ef")
    return metrics