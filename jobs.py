import csv
import random

JOBS = dict()

def readFile() :
    with open('occupations.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        global JOBS
        for row in reader:
            JOBS.update({row['Job Class']:
                         float(row['Percentage'])})
#        del JOBS["Total"]

def randomJob() :
    select = random.random() * JOBS["Total"];
    for x in JOBS :
        if x == "Total" :
            hey = "ignore me"
        elif (select < 0) :
            return x
        else :
            select = select - JOBS[x]
                    
readFile()
print JOBS
print(randomJob())
#print JOBS


