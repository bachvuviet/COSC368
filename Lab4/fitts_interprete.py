# main.py
# Author: Bach Vu
# Window Class

import math
import csv

RECORDS_RAW = {}    # (A, W, selectNo): time
OUTPUT = {}
ID_mean = {}

class FittRecord:
    def __init__(self, a, w):
        self.A = a  # amplitude
        self.W = w  # width
        self.trials = [] # time
        
    def getID(self):
        return math.log2(self.A/self.W + 1)
    
    def addTrial(self, data):
        self.trials.append(data)
    
    def getMean(self):
        mean = sum(self.trials[2:]) / (len(self.trials)-2) # discard first 2 trials, outliner
        return round(mean/1000, 3)
    
    def toString(self):
        Id = round(self.getID(), 2)
        return [self.A, self.W, Id, self.getMean()]

def LoadData():
    #filename = input("Experiment csv: ")
    filename = "experiment_fitts_log.txt"
    with open(filename, mode='r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter = '\t')
        for row in csv_reader:
            key = (int(row[1]), int(row[2]), int(row[3]))
            RECORDS_RAW[key] = float(row[4])
    
def Calculation():
    for desc, time in RECORDS_RAW.items():
        key = (desc[0], desc[1]) 
        record = OUTPUT.get(key, FittRecord(desc[0], desc[1]))
        record.addTrial(time)
        OUTPUT[key] = record
    
    for record in OUTPUT.values(): 
        difficult = round(record.getID(), 3)
        val = ID_mean.get(difficult, [])
        val.append(record.getMean())
        ID_mean[difficult] = val
    
def WriteOutput():
    filename = "summary.csv"
    with open(filename, mode='w') as record_file:
        csv_writer = csv.writer(record_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_NONE)
        csv_writer.writerow(['A','W','ID','mean time'])
        for record in OUTPUT.values():                         
            csv_writer.writerow(record.toString())       
            
        csv_writer.writerow(['ID','mean time'])
        for Id, time in ID_mean.items():       
            mean = round(sum(time)/len(time), 3)
            csv_writer.writerow([Id, mean])          
        
    
if __name__ == "__main__":
    LoadData()
    Calculation()
    WriteOutput()