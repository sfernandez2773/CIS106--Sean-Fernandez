A= input("Do you want to begin the tuition cost calculator? (Yes or No)")
LastName = input("Please enter the student's last name")
Credit = int (input("Please enter the student's credit hours"))
DistrictCode = input("Please enter the student's district code")
I=250
O=550
#Determining the student's district code
#Find the student's total tuition cost based on the district code and credit hours
TuitionCost = Credit * I
def TuitionCost (Credit, I, O):
    if DistrictCode == "I":
        TuitionCost = Credit * I
    elif DistrictCode == "O":
        TuitionCost = Credit * O
    else:
        print("Please enter a valid district code")
    return TuitionCost
def DistrictCode (I,O):
    if DistrictCode == "I":
        TuitionCost = Credit * I
    elif DistrictCode == "O":
        TuitionCost = Credit * O
    else:
        print("Please enter a valid district code")
    return TuitionCost

print ("The student's last name is", LastName)
print ("The student's credit hours are", Credit)
print ("The student's district code is", DistrictCode)
print ("The total tuition cost", TuitionCost)



     