#input
LastName= input("Enter the employee's last name")
Salary = int (input("Enter your salary"))
JobLevel = int (input("Enter your job level"))

#Process
if JobLevel >= 10:
    Bonus = 0.25
elif JobLevel >= 5 and JobLevel <= 9:
    Bonus = 0.20
else:
    Bonus = 0.10

Bonus= float(Salary * Bonus)

#Output
print("Employee's last name is:", LastName)
print("The Employee's bonus is:", Bonus)

    