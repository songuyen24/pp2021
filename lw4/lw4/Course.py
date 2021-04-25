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
    