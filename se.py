#!/usr/bin/python3

import utilities

MIN_COLUMNS_TO_MATCH = 7

reader1 = utilities.lowerCSV(utilities.readCSV('1.csv'))
reader2 = utilities.lowerCSV(utilities.readCSV('2.csv'))

matchings, total_matched_items1, total_matched_items2 = utilities.match_data(reader1, reader2, MIN_COLUMNS_TO_MATCH)

print(matchings)
print(len(matchings))

utilities.write_matches_csv('machings.csv', matchings, reader1, reader2)

utilities.write_no_matches_csv('nomatches1.csv', reader1, total_matched_items1)
utilities.write_no_matches_csv('nomatches2.csv', reader2, total_matched_items2)
