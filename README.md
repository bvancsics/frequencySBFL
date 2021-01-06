# frequencySBFL
Call Frequency-Based Fault Localization

Run: python -W ignore main.py --cov-folder=[trace-folder]/coverage/ --nameMapping=[trace-folder]/coverage/trace.trc.names --change=./changed_methods/[project]-changes.csv --bugID=[ID]
For example: python -W ignore main.py --cov-folder=./Lang/Lang-1b-chain-count/coverage/ --nameMapping=./Lang/Lang-1b-chain-count/coverage/trace.trc.names --change=./changed_methods/Lang-changes.csv --bugID=1
