AM = input("Do you want to begin? (Yes or No) ")
LastName = input("Enter the employee's last name")
JobCode = (input("Enter the employee's job code (L, A, or J)"))

HoursWorked = int (input("Enter the amount of hours the employee worked"))

#processing

def Payrate(JobCode):
    if JobCode == "L":
        return 25.00
    elif JobCode == "A":
        return 30.00
    elif JobCode == "J":
        return 35.00
    else:
        print("Invalid job code")
        return 0.00


A= input("Do you want to continue? (Yes or No) ")

print("The employee's gross pay is", Payrate(JobCode) * HoursWorked)
print("The employee's gross pay is", Payrate)
 


