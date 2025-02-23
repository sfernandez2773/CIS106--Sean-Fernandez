#input
Quantity = int (input("Enter amount of concert tickets"))

#process
if Quantity >= 25:
    PricePerTicket = 50
    Total = Quantity * PricePerTicket
elif Quantity >= 10:
    PricePerTicket = 60
    Total = Quantity * PricePerTicket
elif Quantity >= 5 and Quantity <= 9:
    PricePerTicket = 70
    Total = Quantity * PricePerTicket
else:
    PricePerTicket = 75
    Total = Quantity * PricePerTicket
Total = Quantity * PricePerTicket

#Output
print("The total cost of the tickets" , Total)
print(" The price per ticket is" , PricePerTicket)
print(" The number of tickets purchased is", Quantity)


