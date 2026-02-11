from grade_compute import *

## Validates proper input and parses grades
def validate_input(grade_str):
    if grade_str.upper() == 'Q':
        return None

    parts = grade_str.split('$')

    if len(parts) != 4:
        return None
    
    valid_bases = ['A', 'B', 'C', 'D', 'F']

    for p in parts:
        clean_p = p.strip().upper()

        if not clean_p:
            return None

        if clean_p[0] not in valid_bases:
            return None

        if len(clean_p) == 2 and clean_p[1] not in ['+', '-']:
            return None

    return [g.strip().upper() for g in parts]

# Formatting in ASCII Box
def printReport(grades, lowestGrade, numAvg, letterAvg):
    print("-" * 40)
    print("|{:^38}|".format("GRADE REPORT SUMMARY"))
    print("-" * 40)
    print("| {:<37}|".format("Grades Entered: " + ", ".join(grades)))
    print("| {:<37}|".format("Lowest Grade Dropped: " + lowestGrade))
    print("| {:<37}|".format("Calculated Average: " + f"{numAvg:.2f}"))
    print("| {:<37}|".format("Final Letter Grade: " + letterAvg))
    print("-" * 40)


## User Input Prompt
def processLine():
    prompt = input("Enter 4 letter grades sepearted by $ (or Q to quit): ")

    passed = validate_input(prompt)

    if passed is None:
        if prompt.upper() == 'Q':
            return False
        
        print("Invalid input. Please try again.\n")
        return True
    
    numberGrades = []
    
    for g in passed:
        numberGrades.append(letterToNum(g))

    lowestNumber = lowestGrade(numberGrades)
    lowestLetter = numToLetter(lowestNumber)

    tempList = numberGrades.copy()
    tempList.remove(lowestNumber)

    gpa = calcGPA(numberGrades.copy())
    gpa = curveCheck(tempList, gpa)

    letterAvg = numToLetter(gpa)

    printReport(passed, lowestLetter, gpa, letterAvg)

## Main Executable
def main():
    programOpen = True
    
    while programOpen:
        programOpen = processLine()

## Program Access
if __name__ == "__main__":
    main()
    