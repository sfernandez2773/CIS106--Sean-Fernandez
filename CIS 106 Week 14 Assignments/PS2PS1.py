class Student:
    def __init__(self, FirstName, LastName, DistrictCode):
        self.FirstName = FirstName
        self.LastName = LastName
        self.DistrictCode = DistrictCode

    def Tuition(self):
        if self.DistrictCode == "I":
            return 250.00
        elif self.DistrictCode == "O":
            return 500.00


FirstName = input("Enter First Name: ")
LastName = input("Enter Last Name: ")
DistrictCode = input("Enter District Code (I for In-District, O for Out-of-District): ")
student = Student(FirstName, LastName, DistrictCode)
   
print("Student Name: ", FirstName, LastName)
print("District Code: ", DistrictCode)
print("Tuition: ", student.Tuition())
