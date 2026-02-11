## Takes a letter grade and converts it to the 4.0 grading scale
def letterToNum(grade):
    grade = grade.upper()

    num = 0.0

    if grade[0] == 'A':
        num = 4.0

    elif grade[0] == 'B':
        num = 3.0
    
    elif grade[0] == 'C':
        num = 2.0
    
    elif grade[0] == 'D':
        num = 1.0
    
    elif grade[0] == 'F':
        num = 0.0
    
    ## Grade + or - scaling
    if len(grade) == 2:
        if grade[1] == '+':
            num += 0.3

        elif grade[1] == '-':
            num -= 0.3
    
    return num

## Changes a number grade to a letter grade
def numToLetter(numGrade):
    if numGrade >= 4.0:
        return "A"
    
    elif numGrade >= 3.7:
        return "A-"
    
    elif numGrade >= 3.3:
        return "B+"
    
    elif numGrade >= 3.0:
        return "B"
    
    elif numGrade >= 2.7:
        return "B-"
    
    elif numGrade >= 2.3:
        return "C+"
    
    elif numGrade >= 2.0:
        return "C"
    
    elif numGrade >= 1.7:
        return "C-"
    
    elif numGrade >= 1.3:
        return "D+"
    
    elif numGrade >= 1.0:
        return "D"
    
    elif numGrade >= 0.7:
        return "D-"
    
    else:
        return "F"


## Finds lowest number grade
def lowestGrade(numGrades):
    return min(numGrades)

## Calculate GPA and drops lowest score
def calcGPA(numGrades):
    gradeToDrop = lowestGrade(numGrades)
    numGrades.remove(gradeToDrop)
    return sum(numGrades) / len(numGrades)

## Curve application
def curveCheck(numGrades, gpa):
    for n in numGrades:
        if n > 2.7:
            return gpa
    
    return gpa + 0.25