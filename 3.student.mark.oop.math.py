from numpy import *
from math import *

StudentList = []
CourseList = []
MarkList = []

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
        

mark = []
totMark = 0
print(end="Enter Number of course: ")
totSub = int(input())

print(end="Enter Marks Obtained in " + str(totSub) + " courses: ")
for i in range(totSub):
    mark.insert(i, int(input()))
	
print(end="Enter Maximum Mark: ")
maxMark = int(input())

for i in range(totSub):
    totMark = totMark + mark[i]
avg = totMark/totSub
perc = (totMark/(totSub*maxMark))*100

print("Average Mark = " + str(avg))
print("Percentage Mark = " + str(perc) + "%")

