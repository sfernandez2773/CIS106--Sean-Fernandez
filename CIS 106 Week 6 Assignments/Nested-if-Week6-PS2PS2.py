#input
PartNumber = int    (input("Enter the part numbers"))
Quantity =  (input("Enter the quantity"))

#process
if PartNumber == 10 or PartNumber == 55:
    UnitPrice = 1.00
elif PartNumber == 99:
    UnitPrice = 2.00
elif PartNumber == 70 or PartNumber == 80:
    UnitPrice = 3.00
else:
    UnitPrice = 5.00

TotalPrice = float (Quantity) * UnitPrice

#output
print("The amount of part numbers is", PartNumber)
print(" The Unit Price is", UnitPrice)
print("The total price is", TotalPrice)