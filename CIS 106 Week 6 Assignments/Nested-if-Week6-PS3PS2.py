#input
Principle =int (input("Enter the Principle amount"))
Years = int(input("Enter the number of years"))

#Process
if Principle > 100000:
    if Years == 5:
        Interest = 0.06
    if Principle > 50000:
        Years = 10
        Interest = 0.05
        if Principle > 50000:
            Years = 5
            Interest = 0.04
    else:
        Interest = 0.02

First = Principle * Interest
        
#Output
print("The principle amount is $", Principle)
print("The interest rate is", Interest)
print("The first year total is $", First)

        