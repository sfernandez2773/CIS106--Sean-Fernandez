print("Do you want to begin? (Yes or No)")
Make= input("Enter the Make of the car: ")
MSRP= int(input("Enter the cost of the car: "))
Electric= input("What is the Electric vehicle code? (Yes or No)")


def Make(Honda_Accord, Toyota_Rav4, Electric, Others):
    if Make == Honda_Accord:
        Percent = 0.10
        print("The percent is: ", Percent)
    if Make == Toyota_Rav4:
        Percent = 0.15
        print("The percent is: ", Percent)
    if Make == Electric:
        Percent = 0.30
        print("The percent is: ", Percent)
    if Make == Others:
        Percent = 0.05
        print("The percent is: ", Percent)
    return Percent

def electric(Electric):
    if Electric == "Yes":
        Percent= 0.30
        print("The percent is: ", Percent)
    else:
        Percent= 0.00
        print("The percent is: ", Percent)
    return Percent
def MSRP(MSRP, Percent):
  Total = MSRP - (Percent * MSRP + .07 * MSRP)
  print("The name of the model is: ", Make)
  print("The MSRP is: ", MSRP)
  return Total
print("The total cost is: ", Total)
print("The total cost is: ", Total)
A = input("Do you want to begin? (Yes or No)")
while A.lower() == "yes":
    Honda_Accord = "Honda Accord"
    Toyota_Rav4 = "Toyota Rav4"
    Others = "Others"
    Percent = Make(Honda_Accord, Toyota_Rav4, Electric, Others)
    electric_percent = electric(Electric)
    Total = MSRP(MSRP, Percent)
    print("The total cost is: ", Total)
    A = input("Do you want to continue? (Yes or No)")
else:
    print("The program has ended")
    exit()