import csv
from itertools import chain, combinations, groupby
from collections import defaultdict

def readCSV(filename):
    with open(filename, newline='') as f:
        contents = csv.reader(f)
        
        # we need to read the contents of the file into memory
        return [row for row in contents]

def lowerCSV(contents):
    return [list(map(lambda x: x.lower(), row)) for row in contents]

def powerset(s, min_columns):
    p = list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
    p.reverse()
    # we only want a match if there are 2 or more column matches
    return filter(lambda x: len(x) >= min_columns, p)

def match_data(contents1, contents2, min_columns):
    matchings = defaultdict(list)

    num_columns = len(contents1[0])

    # need to reverse order and remove []
    column_lists = powerset(list(range(num_columns)), min_columns)

    total_matched_items1 = set()
    total_matched_items2 = set()

    for key, column_lists in groupby(column_lists, len):
        # store these since we want multiple matches for the same column lengths
        temp_matched_items1 = set()
        temp_matched_items2 = set()
        
        remaining_items1 = set(range(len(contents1))).difference(total_matched_items1)
        remaining_items2 = set(range(len(contents2))).difference(total_matched_items2)
        
        for column_list in column_lists:
            print(column_list)

            for i in remaining_items1:
                c1_row = contents1[i]

                relevant_col1 = [c1_row[r] for r in column_list]

                if not all(relevant_col1):
                    continue

                matchings_for_i = []

                for j in remaining_items2:
                    c2_row = contents2[j]

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

    return (matchings, total_matched_items1, total_matched_items2)

def write_no_matches_csv(filename, contents, matched_items):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        
        remaining_items = set(range(len(contents))).difference(matched_items)
        
        for remaining_item in remaining_items:
            writer.writerow(contents[remaining_item])
