#Creating car class

class car:
    def Name(Self):
        Self.name = input("Enter the name of the car: ")
        print("The name of the car is: ", Self.name)
        
    def Model(Self):
        Self.model = input("Enter the model of the car: ")
        print("The model of the car is: ", Self.model)
    def Price(Self):
        Self.price = input("Enter the price of the car: ")
        print("The price of the car is: ", Self.price)
    def Discount(Self):
        Self.Discount = input("Enter the discount of the car: ")
        print("The discount of the car is: ", Self.Discount)
    def include_sports_features(Self):
        A = input("Do you want to include sports features? (Y or N): ")
        if A == "Y":
            print("The car has sports features added")
        elif A == "N":
            print("The car will not have sports features included")
        else:
            print("Invalid input")


    #inheriting from car 
class CarSport(car):
    def SportWheel(Self):
        Self.sportwheel = input("Enter the sport wheel's cost 1.0000.00.")
        print("The sport wheel's cost is: ", Self.sportwheel)
    def SportEngine(Self):
        Self.sportengine = input("Enter the sport engine's cost is 3.0000.00. ")
        print("The sport engine's cost is: ", Self.sportengine)
    def SportInterior(Self):
        Self.Discount= input("The sport interior's cost is 2.0000.00.")
        print("The sport interior's cost is: ", Self.sportinterior)

