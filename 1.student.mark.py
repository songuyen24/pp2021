print("Student mark management")

numberStudent = int(input("Enter number of student: "));
print("Class has:", numberStudent, "student")
studentDict = {}
def inputstudent(id, name, dob):
    studentDict[id] = [name, dob]
for i in range(numberStudent):
    print(i+1, "st Student")
    a = input("Id: ")
    b = input("Name: ")
    c = input('Dob: ')
    inputstudent(a, b, c)
    
def showStudents():
    "student list"
    print("Student list")
    global numberStudent
    for i in range(0, len(numberStudent)):
        print("[",numberStudent[i]['id'],"]", "[",numberStudent[i]['name'],"]",)
def courseNumber(id, name):
 for i in range(numberCourse):
    print(i+1, "course")
    a = input("Id:")
    b = input("Name:")
    printCourse(a, b)
    
def studentMark():
    global numberStudent
    print("Enter Student id to input mark")
    id = input()
    student = findStudent(id)
    if student == False:
        print("Student not found")
    else :
        print("enter student name")
        name = input()
        student[1]['name'] = name
        numberStudent[student[0]] = student[1]
 
    a = "Student Mark"
    input()
    markSum = input("Mark: ")
    print("Student mark:")

numberStudent = []
action = 0
 
while action >= 0:
    if action == 1:
        showStudents()
    elif action == 2:
        studentMark()
    
 
    print("Choose an option")
    print("Input 1: Student List")
    print("Input 2: Student's mark")
    print("Input 0: exit the program")
    action = int(input())
    if action == 0:
        break

