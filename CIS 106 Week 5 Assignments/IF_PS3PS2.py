#input
Books= input("Enter the number of books")
Cost = float(input("Enter the cost of the books"))
#process
Total = Cost + int(Books)

if Total > 50:
    FreeShippingTotal = Total + 0
    #output 
    # print("You qualify for free shipping")
else:
    Total = Total + 25
#output
# print("You do not qualify for free shipping")

#output
print("The total cost of the books is $", Total)
print("The total cost of the books with shipping is $", Total)
