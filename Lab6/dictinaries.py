def getStudent(directory, student):
    return directory[student]


def getStudentGrades(directory, student):
    return directory[student]["grades"]


def getStudentGradeLevel(directory,student):
    return directory[student]["gradelevel"]

def getStudentEmail(directory,student):
    return directory[student]["studentemail"]


def getStudentsByGradeLevel(directory, gradelevel):
    for student in directory:
        if directory[student]["gradelevel"] == gradelevel:
            print(directory[student])
    
def addStudent(directory):
    student = {}
    name = input("What is the name of the new student?").strip()
    gradelevel = int(input("What is the gradelevel of said student?"))
    email = input("what is the email od said student?").strip()
    englishgrade = int(input("what is the english grade of the student?"))
    mathgrade = int(input("what is the math grade of the student?"))
    historygrade = int(input("what is the history grade of the student?"))
    religiongrade = int(input("what is the religion grade of the student?"))
    grades = {"math":mathgrade,"history":historygrade,"religion":religiongrade,"english":englishgrade}
    student["email"] = email
    student["gradelevel"] = gradelevel
    student["grades"] = grades
    directory[name] = student


def removeStudent(directory, student):
    directory.pop(student)
def updateGrade(directory, student):
    for grade in directory[student]["grades"]:
        directory[student]["grades"][grade] = int(input(f"what is the new grade for {grade}?"))
        
    

def calculateGPA(directory, student):
    GPA = 0
    for grades in directory[student]["grades"]:
        GPA += directory[student]["grades"][grades]
        
    GPA/= len(directory[student]["grades"])
    return print(f"{GPA} is the average of all grades")


def checkHonorRoll(directory,student):
    """
     Function Name: checkHonorRoll
        Parameters:
            Directory <dict> : Student Directory that is specified in the main() function
            student <String> : String that corresponds to the student name
            Return Type:  <bool> True or False depending on a student has made the honor roll or not
        Description:
            Calls the calculateGPA() subroutine that gets the GPA then checks all grades in the grade book to see if they are all over 81, then returns True or False depending on if the GPA is 88 or better
    """
    GPA = calculateGPA(directory,student)
    for grades in directory[student]["grades"][grades]:
        if grades <= 81:
            directory[student]["calculateGPA"]
    pass

def printMenu():
    print("Welcome to Calvet Hall Student Directory")
    print("1. Add student")
    print("2. Remove Student")
    print("3. Get Student")
    print("4. update grades")
    print("5. calculate GPA")
    print("6. Get students grade level")
    print("7. Exit")
    option = input("What option would you like?")
    return option

def main():
    #TODO: Implement every function in main
    
    Students = {}
    addStudent(Students)
    print(Students)
    print(Students["nick"])
    print(Students["nick"]["grades"])
    print(Students["nick"]["grades"]["history"])
if __name__ == "__main__":
    main()

