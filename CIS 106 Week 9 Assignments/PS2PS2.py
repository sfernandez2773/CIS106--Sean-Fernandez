#input
LastName = input("Enter the player's name: ")
NumberHits = int(input("Enter the amount of hits the player has made: "))
AtBats = int(input("Enter the amount of times the player has batted: "))
#processing
BattingAverage = NumberHits / AtBats
def divide(NumberHits, AtBats):
    print("The batting average is: " + str(BattingAverage))
divide(NumberHits, AtBats)
#output
print(f"Player's name: {LastName}")
print(f"Number of hits: {NumberHits}")
print(f"Number of at bats: {AtBats}")
print(f"Batting Average: {BattingAverage:.3f}")

A = input("Do you want to continue? (Yes or No) ")
if A == "Yes":
    LastName = input("Enter the player's name: ")
    NumberHits = int(input("Enter the amount of hits the player has made: "))
    AtBats = int(input("Enter the amount of times the player has batted: "))
    BattingAverage = NumberHits / AtBats
    def divide(NumberHits, AtBats):
        print("The batting average is: " + str(BattingAverage))
    divide(NumberHits, AtBats)
    print(f"Player's name: {LastName}")
    print(f"Number of hits: {NumberHits}")
    print(f"Number of at bats: {AtBats}")
    print(f"Batting Average: {BattingAverage:.3f}")