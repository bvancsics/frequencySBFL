from base import Coverage, Ranks, ArgumentumParser

param_dict = ArgumentumParser.arg_parser()
metrics = ArgumentumParser.get_metrics()

cov = Coverage.Coverage(param_dict["naive-folder"],
                        param_dict["naive-mapper"],
                        param_dict["unique-folder"],
                        param_dict["unique-mapper"])

cov.set_coverage_data(param_dict["change"],
                      param_dict["bugID"])

rankContainer = Ranks.RankContainer(cov, metrics)
rankContainer.add_ranks(param_dict["bugID"], param_dict["rank-method"])
rankContainer.printMinRanks(param_dict["bugID"])
