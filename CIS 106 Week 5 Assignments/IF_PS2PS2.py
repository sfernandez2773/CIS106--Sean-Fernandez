#input
UnitPrice = input("Enter an item")
Quantity = input("Enter the Quantity") 
#process
ExtendedPrice = float (Quantity) * float (UnitPrice)
if UnitPrice == "10.00":
	UnitPrice = "10.00"
else:
	UnitPrice = "20.00"


#output
print("The item choose is ", UnitPrice)
print("The Quantity is", Quantity)  
print("The Extended Price is", ExtendedPrice)
