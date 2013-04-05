import csv

def readCSV(filename):
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        
        return [list(x) for x in reader]

def lowerCSV(contents):
    return [map(lambda x: x.lower(), row) for row in contents]