import argparse

def arg_parser():
    parser = argparse.ArgumentParser(description = 'frequency-based fl')
    parser.add_argument('-c', '--cov-folder', required=True, help='coverage folder')
    parser.add_argument('-x', '--change', required=True, help='changes file')
    parser.add_argument('-b', '--bugID', required=True, help='defects4j bugID')
    parser.add_argument('-m', '--nameMapping', required=True, help='id - method-name pairs')

    param_dict = {}
    args = parser.parse_args()
    param_dict["cov-folder"] = args.cov_folder
    param_dict["change"] = args.change
    param_dict["bugID"] = args.bugID
    param_dict["nameMapping"] = args.nameMapping

    return param_dict


