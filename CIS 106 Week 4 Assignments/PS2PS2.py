#input
Price = float(input("Enter the purchase price per share"))
Current = float(input("Enter the current stock price"))
Quantity = int(input("Enter the number of shares"))

#process
StockValue =(Price- Current) * Quantity

#Output
print("The total value of the stock is $", StockValue)
