#input
def DiscountTotal(Quantity, Price, Discount):
    Total = Quantity * Price
    DiscountedTotal = Total - Discount
    Discount= Total * Discount
    return DiscountedTotal

print("Enter the Quantity of the item: ")
Quantity = int(input())
print("Enter the Price of the item: ")
Price = float(input())
print("Enter the Discount: ")
Discount = float(input())
print("The Discounted Total is $: ", DiscountTotal(Quantity, Price, Discount))

