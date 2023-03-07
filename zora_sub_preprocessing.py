#!/usr/bin/env python3
# *-* coding: UTF-8 *-*
# Author: Jessica Roady

from langdetect import detect

# # OLD
# with open("data/robin_data.tsv") as f:
#     rows = []
#     rows_before_rstrip = []
#     rows_after_rstrip = []
#     rows_after_tsplit = []
#
#     for line in f:
#         rows_before_rstrip.append(line)
#         line = line.rstrip("\n")
#         rows_after_rstrip.append(line)
#         row = line.split("\t")
#         rows_after_tsplit.append(row)
#
#         # Only those with abstracts
#         if row[-1] != "":
#             if row[-1] == "\"":
#                 print(row)
#                 # print(num_after_tsplit)
#             else:
#                 if detect(row[-1]) == "en":
#                     rows.append(row)
#
# rows.pop(0)
#
# fuck_ups = 0
# for i in rows:
#     if len(i) != 7:
#         fuck_ups += 1
#         print(i)
#
# print(f"Num. rows: {len(rows)}")
# print(f"Num. fuck-ups: {fuck_ups}")
# print(f"Num. non-fuck-ups: {len(rows) - fuck_ups}")
#
# print(len(rows_before_rstrip))
# print(len(rows_after_rstrip))
# print(len(rows_after_tsplit))

# for i in rows:
#     print(i)

with open("data/robin_data.tsv") as f:
    rows = []
    row_id = 0

    for line in f:
        line = line.rstrip("\n")
        row = line.split("\t")

        # Only those with abstracts
        # TODO: Once buggy rows are fixed, langdetect titles instead of abstracts
        if row[-1] != "" and row[-1] != "\"" and detect(row[-1]) == "en":
            row_id += 1
            row.insert(0, row_id)
            rows.append(row)

# buggy_rows = [i for i in rows if len(i) != 8]
# print([i for i in buggy_rows])
# print(len(buggy_rows))

print(len(rows))
