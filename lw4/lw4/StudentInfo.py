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