# frequencySBFL
Fault Localization Using Function Call Frequencies

Run main.py

    python3 -W ignore main.py \
        --naive-folder=[output folder]/naive-coverage/ \
        --naive-mapper=[output folder]/naive-coverage/trace.trc.names \
        --unique-folder=[output folder]/unique-coverage/ \
        --unique-mapper=[output folder]/unique-coverage/trace.trc.names \
        --change=./changed_methods/Lang-changes.csv \
        --bugID=[bug]

For example:

      python3 -W ignore main.py \
          --naive-folder=/sbfl/Lang_1b/naive-coverage/ \
          --naive-mapper=/sbfl/Lang_1b/naive-coverage/trace.trc.names \
          --unique-folder=/sbfl/Lang_1b/unique-coverage/ \
          --unique-mapper=/sbfl/Lang_1b/unique-coverage/trace.trc.names \
          --change=./changed_methods/Lang-changes.csv \
          --bugID=1
