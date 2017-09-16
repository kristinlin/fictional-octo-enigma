# Fabiha Ahmed & Kristin Lin
# SoftDev pd09
# Work03 : Files Occupy Space
# 09-15-17

import csv
import random

# create dictionary
JOBS = dict()


# reads file occupations.csv as csvfile and updates JOBS with Job class as key
# and percentage as value typecasted as a float.

def readFile() :
    with open('occupations.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        global JOBS
        for row in reader:
            JOBS.update({row['Job Class']:
                         float(row['Percentage'])})

            
# Total is 99.8, so any number from 0 to 99.8, not included, is randomly chosen
# We imagined that each of the sections actually held a portion of that 99.8.
# For example, Protective Services is 2.8 percent, but it could represent 34.7
# to 37.5 percent of 99.8 or 71.2 to 74 percent of 99.8.
# Therefore, we used that random number and continuously subtracted each key
# value until the random number became negative, which means that that key is
# chosen

def randomJob() :
    select = random.random() * JOBS["Total"];
    # print select
    for x in JOBS :
        if x == "Total" :
            select = select
            # nothing happens; no one cares about total
        elif (select - JOBS[x] < 0) :
            return x
        else :
            select = select - JOBS[x]


#-------------------------------------------
                    
readFile()
#print JOBS
print(randomJob())



