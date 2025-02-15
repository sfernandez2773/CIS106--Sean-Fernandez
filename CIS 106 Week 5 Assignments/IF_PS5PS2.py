#input
LastName = input("Enter your last name: ")
GrossIncome = float(input("Enter your Gross Pay amount: "))
Dependents = int(input("Enter the number of dependents: "))
#process 
AdjustedGrossIncome = GrossIncome - 12000.00 * Dependents

if AdjustedGrossIncome > 50000.00:
    tax = AdjustedGrossIncome * 0.20
else:
    tax = AdjustedGrossIncome * 0.10

if tax < 0:
    tax = 100.00

print("Your last name is", LastName)
print("Your Gross Income is $", GrossIncome)
print("Your number of dependents is", Dependents)
print("Your adjusted gross income is $", AdjustedGrossIncome)
print("Your tax is $", tax)