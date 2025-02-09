#input
MealTotal = float(input("Enter the Meal Total: "))
Tip = (0.15, 0.18, 0.20)

#process
for tip in Tip:
    TipAmount = MealTotal * tip
    TotalWithTip = MealTotal + TipAmount
    
    
    #output
    print(f"With a {int(tip * 100)}% Tip:")
    print(f"Meal Total: {MealTotal:.2f}")
    print(f"Tip: {TipAmount:.2f}")
    print(f"Total with Tip: {TotalWithTip:.2f}")
    print()  # for spacing between different tip outputs
      
      

