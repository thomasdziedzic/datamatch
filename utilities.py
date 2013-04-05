import csv

def readCSV(filename):
    with open(filename, newline='') as f:
        contents = csv.reader(f)
        
        # we need to read the contents of the file into memory
        return [row for row in contents]

def lowerCSV(contents):
    return [list(map(lambda x: x.lower(), row)) for row in contents]