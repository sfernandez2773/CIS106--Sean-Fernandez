#input
City = input("Enter the city")
Miles = int(input("Enter the total miles"))
Gallons = int(input("Enter the total gallons used"))
#processing
def divide (Miles, Gallons):
    print("The miles per gallon is", Miles / Gallons)
#output
print(f"The city is", City)
print(f"The total miles is", Miles)
print(f"The total gallons used is", Gallons)
divide(Miles, Gallons)
A = input("Do you want to continue? (Yes or No) ")
if A == "Yes":
    City = input("Enter the city")
    Miles = int(input("Enter the total miles"))
    Gallons = int(input("Enter the total gallons used"))
    def divide (Miles, Gallons):
        print("The miles per gallon is", Miles / Gallons)
    print(f"The city is", City)
    print(f"The total miles is", Miles)
    print(f"The total gallons used is", Gallons)
    divide(Miles, Gallons)
