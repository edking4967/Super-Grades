import json
import time
import csv

def save(filename, struct):
    f = open(filename + str(time.time()) + '.json', 'w')
    f.write(json.dumps(struct))
    f.close()

def load(filename):
    f = open(filename, 'r')
    j = json.loads(f.read())
    f.close()
    return j

def writeToSheet(filename, stuff):
    return 
