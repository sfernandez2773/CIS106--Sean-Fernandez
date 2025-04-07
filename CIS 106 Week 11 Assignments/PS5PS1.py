def Total(Quantity, UnitPrice):
	Tax = 0.07
	Total = Quantity * UnitPrice
	Total = Total + (Total * Tax)
	return Total, Tax

Quantity= float(input("Enter the Quantity: "))
UnitPrice = float(input("Enter the Unit Price: "))

total, tax = Total(Quantity, UnitPrice)

print(f"The total is ${total}")
print("The tax total is $", tax)

