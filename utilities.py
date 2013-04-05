import csv

def readCSV(filename):
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        
        return [list(x) for x in reader]