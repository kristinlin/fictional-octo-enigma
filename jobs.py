import csv
JOBS = dict()

def readFile() :
    with open('occupations.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        global JOBS
        for row in reader:
            JOBS.update({row['Job Class']:
                         float(row['Percentage'])})
    

            
            
readFile()
print JOBS


