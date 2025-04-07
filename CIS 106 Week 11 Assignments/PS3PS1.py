def CommissionTotal(Commission):
    if Commission < 100000:
        Each = 0.10
    else:
        Each = 0.05
    Total = Commission * Each
    Next = Commission * 1.05
    return Total, Next

LastName = input("Enter your last name: ")
Commission = float(input("Enter your commission amount: "))
Total, Next = CommissionTotal(Commission)
print(f"This is the total commission amount: ${Total}")
print(f"This is next year's total commission amount: ${Next}")


        
