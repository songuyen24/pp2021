def studentNumber():
    global studentNumber
    studentNumber = int(input("number of student :"))
def Course():
    global Course
    Course = int(input("number of course : "))
def StudentMark():
    global StudentMark
    StudentMark = int(input("student's mark : "))
    
    
class StudentInformation():
    def __init__(self, ID, name, Dob):
        self.ID = ID
        self.name = name
        self.Dob = dob
    def getStudentInfo(self):
        print("ID : " + self.ID)
        print("Name : " + self.name)
        print("Dob : " + self.Dob)
    def setStudentInfo(self, ID, name, Dob):
        self.ID = ID
        self.name = name
        self.Dob = Dob
        
class Course():
    def __init__(self, name, ID, number):
        self.name = name
        self.ID = ID
        self.number = number
    def getCourseInfo(self):
        print("Name : " + self.name)
        print("ID : " + self.ID)
        print("number :" + self.number)
    def setCourseInfo(self, name, ID, number):
        self.name = name
        self.ID = ID
        self.number = number
    
class StudentMark():
    
    def __init__(self, studentName, Mark, Course):
        self.studentName = studentName
        self.Mark = Mark
        self.course = course
    def getMarkInfo():
        print("studentName :" + self.studentName)
        print("Mark :" + self.Mark)
        print("course :" + self.course)
    def setMarkInfo(self, studentName, Mark, Course):
        self.studentName = studentName
        self.Mark = Mark
        self.course = course
