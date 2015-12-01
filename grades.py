#!/usr/bin/python

import datetime
import json

class HasKey:
    key = 0

class Date:
    year = 0
    month = 0
    day = 0

    def __init__(__self__):  # doesn't work
        year = 0
        month = 0
        day = 0

    def __init__(__self__, y, m, d):
        year = y
        month = m
        day = d


class Student(HasKey):
    englishNames = [] # array of strings for English names
    chineseName = "" # string for Chinese name. [use as key?]
    key = chineseName
    
class Assignment(HasKey):
    name = ""
    grade = '' # Aa Bb Cc Dd Ee Ff
    notes = ""
    #dateAssigned = datetime.date  # date(year,month,day) # Not serializable!
    dateAssigned = Date(0,0,0) # hack until argumentless constructor works
    key = dateAssigned

a1 = Assignment()

a1.name = "assignment 1"
a1.notes= "crazy ol assignment "
a1.dateAssigned = (2015,9,8)

print(a1.name)
print(a1.grade)
print(a1.key)

json.dumps(a1.__dict__)
