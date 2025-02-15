#input
Name = input("Enter name of appliance")
Cost= float (input("How much is the appliance"))


#process
if Cost >= 1000:
    warranty = 0.10 * Cost
    print("Warranty cost is 10% of the price")
else:
    warranty = 0.05 * Cost
    print("Warranty cost is 5% of the price")

Total = warranty + float(Cost)

#output
print("The name of the appliance is", Name)
print("The cost of the appliance is $", Cost)
print("The warranty cost is $", warranty)