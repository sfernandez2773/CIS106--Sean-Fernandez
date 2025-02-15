# input
Quantity = float(input("Enter the quantity of the item: "))
UnitPrice = float(input("Enter the unit price: "))

# process
if Quantity > 1000:
    UnitPrice = 3.00
    print("if Quantity is greater than or equal to 1000, the unit price should be $3.00")
else:
    UnitPrice = 5.00
    print("if Quantity is less than 1000, the unit price should be $5.00")

ExtendedPrice = Quantity * UnitPrice
Tax = ExtendedPrice * 0.07
TotalPrice = ExtendedPrice + Tax

# output
print(f"Extended Price: ${ExtendedPrice:.2f}")
print(f"Tax: ${Tax:.2f}")
print(f"Total Price: ${TotalPrice:.2f}")

    