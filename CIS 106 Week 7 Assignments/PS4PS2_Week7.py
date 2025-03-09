LastName= input("Enter employee's last name")
Hours = int (input("How many hours employee worked"))
Pay = int (input("How much employee gets paid per hour"))
Continue = input("Do you want to continue? (Yes or no)")
while input("Do you want to continue? (Yes or no)") == "Yes":
    #Before we start
    print("Please enter your employee last name and information")
    #Input
    LastName = input("Enter employee's last name: ")
    Hours = int(input("How many hours did the employee work? "))
    Pay = int(input("How much does the employee get paid per hour? "))
    #Process
    if Hours >=40:
        GrossPay = (40 * Pay) + ((Hours - 40) * (1.5 * Pay))
    else:
        GrossPay = Hours * Pay
    #Output
    print("The employee's last name is: ", LastName)
    print("The employee's gross pay is: ", GrossPay)
    print("The employee's hours worked is: ", Hours)