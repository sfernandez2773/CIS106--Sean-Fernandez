#Finding the calculated prices

def ComputedExtendedPrice(Quantity, UnitPrice):
	ExtendedPrice = Quantity * UnitPrice

	if ExtendedPrice > 10000.00:
		Discount = 0.0

	return ExtendedPrice

TotalExtendedPrice = 0.0
A = input("Do you want to calculate the extended price? (Yes or No)")
while A == "Yes":
	Quantity = float(input("Enter the quantity: "))
	UnitPrice = float(input("Enter the unit price: "))
	ExtendedPrice = ComputedExtendedPrice(Quantity, UnitPrice)
	TotalExtendedPrice = TotalExtendedPrice + ExtendedPrice
	print(f"Extended Price is ${ExtendedPrice}")
	A = input("Do you want to calculate the extended price amount (Yes or No): ")