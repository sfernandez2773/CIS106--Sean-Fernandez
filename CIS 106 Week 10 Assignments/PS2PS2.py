A = input("Do you want to begin the program? (Yes or No) ")
if A.lower() == "yes":
    Length = int(input("Enter the length amount: "))
    Width = int(input("Enter the width amount: "))
    Height = int(input("Enter the height amount: "))

    def Area(Length, Width, Height):
        area = 2 * (Length * Width + Length * Height + Width * Height)
        print("The area is " + str(area))
        return area

    def Multiply(area):
        surface_area = area / 50
        print("The surface area is " + str(surface_area))
        return surface_area

    area = Area(Length, Width, Height)
    Multiply(area)

    while True:
        E = input("Do you want to continue the program? (Yes or No) ")
        if E.lower() == "yes":
            Length = int(input("Enter the length amount: "))
            Width = int(input("Enter the width amount: "))
            Height = int(input("Enter the height amount: "))
            area = Area(Length, Width, Height)
            Multiply(area)
        else:
            print("The program has ended.")
            break
else:
    print("The program has ended.")
    