
#JOBS = dict()
workTypes = ''


def readFile() :
    global workTypes
    jobLists = open("occupations.csv", "r")
    workTypes = jobLists.read()
    jobLists.close()

def createDict() :
    JOBS = workTypes.split()
    print(JOBS)

readFile()
createDict()


