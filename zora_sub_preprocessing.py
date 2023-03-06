#!/usr/bin/env python3
# *-* coding: UTF-8 *-*
# Author: Jessica Roady

from langdetect import detect

with open("data/robin_data.tsv") as f:
    rows = []
    rows_before_rstrip = []
    rows_after_rstrip = []
    rows_after_tsplit = []

    for line in f:
        rows_before_rstrip.append(line)
        line = line.rstrip("\n")
        rows_after_rstrip.append(line)
        row = line.split("\t")
        rows_after_tsplit.append(row)

        # TODO: Make row IDs

        # Only those with abstracts
        if row[-1] != "":
            # TODO: Find the one that's just a quote mark
            if row[-1] == "\"":
                print(row)
                # print(num_after_tsplit)
            else:
                if detect(row[-1]) == "en":
                    rows.append(row)

rows.pop(0)

fuck_ups = 0
for i in rows:
    if len(i) != 7:
        fuck_ups += 1
        print(i)

print(f"Num. rows: {len(rows)}")
print(f"Num. fuck-ups: {fuck_ups}")
print(f"Num. non-fuck-ups: {len(rows) - fuck_ups}")

print(len(rows_before_rstrip))
print(len(rows_after_rstrip))
print(len(rows_after_tsplit))

# The problem is when there's a newline in the abstract

# for i in rows:
#     print(i)
