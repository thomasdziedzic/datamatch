#!/usr/bin/python3

import csv
from itertools import chain, combinations, groupby
from collections import defaultdict

import utilities

MIN_COLUMNS_TO_MATCH = 2

matchings = defaultdict(list)

def powerset(s):
    p = list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
    p.reverse()
    # we only want a match if there are 2 or more column matches
    return filter(lambda x: len(x) >= MIN_COLUMNS_TO_MATCH, p)

num_columns = 0
with open('1.csv', newline='') as c1:
    # do we really have to do it this way?
    num_columns = len(csv.DictReader(c1).fieldnames)

reader1 = utilities.lowerCSV(utilities.readCSV('1.csv'))
reader2 = utilities.lowerCSV(utilities.readCSV('2.csv'))

# need to reverse order and remove []
column_lists = powerset(list(range(num_columns)))

total_matched_items1 = set()
total_matched_items2 = set()

for key, column_lists in groupby(column_lists, len):
    # store these since we want multiple matches for the same column lengths
    temp_matched_items1 = set()
    temp_matched_items2 = set()
    
    remaining_items1 = set(range(len(reader1))).difference(total_matched_items1)
    remaining_items2 = set(range(len(reader2))).difference(total_matched_items2)
    
    for column_list in column_lists:
        print(column_list)

        for i in remaining_items1:
            c1_row = reader1[i]

            relevant_col1 = [c1_row[r] for r in column_list]

            if not all(relevant_col1):
                continue

            matchings_for_i = []

            for j in remaining_items2:
                c2_row = reader2[j]

                relevant_col2 = [c2_row[r] for r in column_list]
                
                if not all(relevant_col2):
                    continue

                if relevant_col1 == relevant_col2:    
                    matchings_for_i.append(j)

            if len(matchings_for_i):
                matchings[i] += matchings_for_i
                temp_matched_items1.add(i)
                temp_matched_items2.update(matchings_for_i)
                
    total_matched_items1.update(temp_matched_items1)
    total_matched_items2.update(temp_matched_items2)

print(matchings)
print(len(matchings))

out_csv = []
empty_row = [''] * num_columns
with open('matchings.csv', 'w', newline='') as f:
    matchings_writer = csv.writer(f)
    
    for i, i_matchings in matchings.items():
        out_csv.append(reader1[i])
        
        for j in i_matchings:
            out_csv.append(reader2[j])
        
        out_csv.append(empty_row)
        
    
    matchings_writer.writerows(out_csv)

with open('nomatches1.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    
    remaining_items1 = set(range(len(reader1))).difference(total_matched_items1)
    
    for remaining_item1 in remaining_items1:
        writer.writerow(reader1[remaining_item1])

with open('nomatches2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    
    remaining_items2 = set(range(len(reader2))).difference(total_matched_items2)
    
    for remaining_item2 in remaining_items2:
        writer.writerow(reader2[remaining_item2])
