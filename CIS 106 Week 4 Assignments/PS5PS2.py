#input
FixedCost = float ((input("Enter the fixed cost")))
PricePerUnit = float ((input("Enter the price per unit")))
CostPerUnit = float ((input("Enter the Costs per unit")))

#process
Total = FixedCost / (PricePerUnit - CostPerUnit)    

#output
print("The total amount afterwards is $", Total) 