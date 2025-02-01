#input
Make = input("Enter Make of car")
Model = input("Enter Model of car")
Msrp = float (input("Enter MSRP of car"))
Discount = float (input("Enter Discount of the car"))

#Process
DiscountAmount = Msrp - Discount
Total = Msrp / Discount

#Output
print ("The total of the car's price", Total)