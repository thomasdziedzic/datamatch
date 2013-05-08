#!/usr/bin/python3

import csv

import utilities

MIN_COLUMNS_TO_MATCH = 2

reader1 = utilities.lowerCSV(utilities.readCSV('1.csv'))
reader2 = utilities.lowerCSV(utilities.readCSV('2.csv'))

num_columns = len(reader1[0])

matchings, total_matched_items1, total_matched_items2 = utilities.match_data(reader1, reader2, MIN_COLUMNS_TO_MATCH)

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
