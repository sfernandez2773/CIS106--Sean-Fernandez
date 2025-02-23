#input
Quantity = int(input("Enter the amount of Quantity"))

#process
if Quantity > 1000:
    Price = 10
elif Quantity >= 5000 and Quantity <= 1000:
    Price = 20
else:
    Price = 30

ExtendedPrice = Quantity * Price
Tax = ExtendedPrice * 0.07
TotalPrice = ExtendedPrice + Tax

#Output
print("The Extended Price is $", ExtendedPrice)
print("The Tax is", Tax)
print("The Total Price is $", TotalPrice)