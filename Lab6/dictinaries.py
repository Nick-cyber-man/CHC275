def getStudent(directory, student):
    student = {}
    student1 = {}
    student2 = {[student]:10}
    pass

def getStudentGrades(directory, student):
    pass

def getStudentGradeLevel(directory,student):
    """
        Function Name: getStudentGradeLevel
        Parameters:
            Directory <dict> : Student Directory that is specified in the main() function
            student <String> : String that corresponds to the student name
            Return Type:  integer corresponding to student's grade level
        Description:
            A Function that returns a Dictionary of the student's gradebook at dictionary[student]
    """
    pass

def getStudentEmail(directory,student):
    """
        Function Name: getStudentGradeLevel
        Parameters:
            Directory <dict> : Student Directory that is specified in the main() function
            student <String> : String that corresponds to the student name
            Return Type:  string corresponding to student's email
        Description:
            A Function that returns a string of the student's email at dictionary[student]
    """
    pass

def getStudentsByGradeLevel(directory, gradelevel):
    """
        Function Name: getStudentsbyGradeLevel
        Parameters:
            Directory <dict> : Student Directory that is specified in the main() function
            gradelevel <int> : integer corresponding to the grade level
            Return Type:  none
        Description:
            procedure that prints out all of the students of a corresponding grade level.
    """
    pass

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
    """
        Function Name: removeStudent
        Parameters:
            Directory <dict> : Student Directory that is specified in the main() function
            student <String> : String that corresponds to the student name
            Return Type:  none
        Description:
            procedure that removes the student at directory[student]
    """
    pass

def updateGrade(directory, student):
    """
     Function Name: updateGrades
        Parameters:
            Directory <dict> : Student Directory that is specified in the main() function
            student <String> : String that corresponds to the student name
            Return Type:  none
        Description:
            procedure that updates a student's gradebook
    """
    pass


def calculateGPA(directory, student):
    """
     Function Name: calculateGPA
        Parameters:
            Directory <dict> : Student Directory that is specified in the main() function
            student <String> : String that corresponds to the student name
            Return Type:  <float> average of all grades
        Description:
            creates a GPA variable set equal to zero, then computes the average (mean) of all of the grades in the gradebook
    """
    GPA = 0
    pass


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

