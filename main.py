import argumentum_parser
import coverage
import ranks

# For example: python -W ignore main.py
# --cov-folder=./Lang/Lang-1b-chain-count/coverage/
# --nameMapping=./Lang/Lang-1b-chain-count/coverage/trace.trc.names
# --change=./changed_methods/Lang-changes.csv
# --bugID=1

param_dict = argumentum_parser.arg_parser()
metrics = ["Barinel", "Barinel-C",
           "Jaccard", "Jaccard-C",
           "Ochiai", "Ochiai-C",
           "Russell-Rao", "Russell-Rao-C",
           "Sorensen-Dice", "Sorensen-Dice-C"]

print("bugID;"+";".join(metrics))
cov = coverage.Coverage(param_dict["cov-folder"], param_dict["nameMapping"])
cov.set_coverage_data(param_dict["change"], param_dict["bugID"])

rankContainer = ranks.RankContainer(cov, metrics)
rankContainer.add_ranks()

rankContainer.printMinRanks(param_dict["bugID"])
