class StudentInformation():
    def __init__(self, ID, name, Dob):
        self.ID = ID
        self.name = name
        self.Dob = dob
    def StudentInfo(self):
        print("ID : " + self.ID)
        print("Name : " + self.name)
        print("Dob : " + self.Dob)
class Course():
    def __init__(self, name, ID, number):
        self.name = name
        self.ID = ID
        self.number = number
    def CourseInfo(self):
        print("Name : " + self.name)
        print("ID : " + self.ID)
        print("number :" + self.number)
class StudentMark():
    
    def __init__(self, studentName, Mark, Course):
        self.studentName = studentName
        self.Mark = Mark
        self.course = course
    def MarkInfo():
        print("studentName :" + self.studentName)
        print("Mark :" + self.Mark)
        print("course :" + self.course)