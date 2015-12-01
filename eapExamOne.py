#!/usr/bin/python

from fileOps import load
import json


def addGrade(student, grade, theClass):
    try:
        theClass[student].append(grade)
        print theClass[student]
    except KeyError:
        print "New student"
        theClass[student] = [grade]

def addSomeGrades(theClass):
    input = ''
    while input != 'x':
        input = raw_input()
        words = input.split(' ')
        student = words[0]
        for word in words:
            if word != student:
                print ""
        addGrade(words[0], int(words[1]), theClass)

def searchGrades(classList, searchTerm):
    for i,mClass in enumerate(classList):
        try:
            print mClass[searchTerm]
        except KeyError:
            print "No student " + searchTerm + " in class " + str(i+1)

grades = load("gradeOne4PM.json")

totalPoints = 73
def calculateGrade(grades):
    gradeA = []
    for student in grades:
        try:
            if(len(grades[student]) == 4):
                grade = grades[student]
                print grade
                finalGrade = (float(grade[0]) + float(grade[1]) + float(grade[2]) / 4 + float(grade[3])) / float(totalPoints)
                print student + " " +  str(finalGrade)
                gradeA.append(finalGrade)
        except TypeError:
            continue
    return gradeA


calculateGrade(grades)
