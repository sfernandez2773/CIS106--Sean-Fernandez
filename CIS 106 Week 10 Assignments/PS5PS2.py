A= input("Do you want to begin? (Yes or No)")
County= input("Enter the county")
Market= int (input("Enter the market value of the property"))

# Define county names as strings
Cook = "Cook"
Dupage = "Dupage"
McHenry = "McHenry"
Kane = "Kane"
Others = "Others"

def A(Yes, Y):
    if A == Yes or A == Y:
        return True
    else:
        return False
def A(No, N):
    if A == No or A == N:
        return False
    else:
        return True
def Market(Cook, Dupage, McHenry, Kane, Others):
    if County == Cook:
        Value = 0.90
        print ("The value of the property is: ", Value)
        if County == Dupage:
            Value = 0.80
            print ("The value of the property is: ", Value)
            if County == McHenry:
                Value = 0.75
                print ("The value of the property is: ", Value)
                if County == Kane:
                    Value = 0.60
                    print ("The value of the property is: ", Value)
                    if County == Others:
                        Value = 0.70
                        print ("The value of the property is: ", Value)
                        Total(Value, Market)
                        Total = Value * Market
                        return Total
                    return Total
Total = Value * Market
print(" The total value is : ", Total)
def Total(Value, Market):
    Total = Value * Market
    return Total
A_ = input("Do you want to continue? (Yes or No)")
if A("Yes", "Y"):
    print("The value of the property is: ", Total(Market(Cook, Dupage, McHenry, Kane, Others), Market))
else:
    print("Thank you for using the program")
