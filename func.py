array = []
for item in data:
    for subitem in item:
        try:
            if(re.findall("[a-z]", subitem)):
                print subitem
                array.append(subitem)
        except TypeError:
            continue


for item in jasGrades:
    for subitem in item:
           print subitem

array = []
for superitem in data:
    for item in superitem:
        for subitem in item:
            try:
                if(re.findall("[a-z]", subitem)):
                    print subitem
                    array.append(subitem)
            except TypeError:
                continue


import re
def searchInArray(array, searchterm):
    for item in array:
        if(len(re.findall(searchterm, item) > 0)):
            return re.findall(searchterm, item)

def unfold(nested):
    try: 
        len(nested) 
        # nested is nested
        unfold(nested)

    except TypeError:
        # We have reached the bottom
        return
    
n = [1,2,3,[1,2,3,[1,2]]]
# works for lists:
def unfold(n):
    for item in n:
        try:
            len(item)
            unfold(item)
        except TypeError:
            print item

def unfoldDict(d):
    for item in d:
        try:
            print d[item]
        except KeyError:
            print item

def add(student,grade):
    try:
        classThreeData[student] += 0 
        print "student grade already exists"
        try:
            len(classThreeData[student])
            classThreeData[student].append(grade)
        except TypeError: # only one value so far
            classThreeData[student] = [classThreeData[student], grade]
    except KeyError: # no data for this student yet
            classThreeData[student] = grade
    print classThreeData[student]

def addGrade(student, grade, theClass):
    try:
        theClass[student].append(grade)
    except KeyError:
        print "New student"
        theClass[student] = [grade]

def addSomeGrades(theClass):
    input = ''
    while input != 'x':
        input = raw_input()
        words = input.split(' ')
        student = words.pop(words[0])
        theClass[student] = words

for student in sd:
    try:
        len(sd[student][2])
        sd[student][2] = int(sd[student][2][0])
    except IndexError:
        continue
    except TypeError: 
        continue

def getGradesFromFile(filestring):
    lines = filestring.split('\n')
    grammarGrades = []
    essayGrades = []
    mDict = {}
    for line in lines:
        words = line.split(' ')
        student = words[0]
        grammarGrade = int(words[1])
        essayGrade = int(words[2])
        mDict[student] = [essayGrade, grammarGrade]
    return mDict

def lookupStudent(g,s):
    for i,c in enumerate(g):
        try:    
            c[s]
            print s + " is in class " + str(i+1)
        except KeyError:
            continue


for line in class2str.split('\n'):
    try:
        words = line.split(" ")
        student = words[0]
        one = words[1]
        two = words[2]
        three = words[3]
        four = words[4]
        dict[student] = [one, two, three, four]
    except IndexError:
        print "error with " + line

def calculategrades(classdict):
    array = []
    for student in classdict:
        print student
        grade = g[1][student]
        total = (float(grade[0])/16 + float(grade[1])/12 + float(grade[2])/100 + float(grade[3])/20)/4
        print total
        array.append([student, total])
    return array

for student in g[3]:
    for j,grade in enumerate(g[3][student]):
        g[3][student] = int(grade)

def getMean(list):
    mean = 0
    for item in list:
            mean += item
    mean = mean / len(list)
    return mean

