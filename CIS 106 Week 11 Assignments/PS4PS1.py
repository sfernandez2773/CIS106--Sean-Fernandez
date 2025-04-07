def AverageScore(Game1,Game2,Game3,Basis,Handicap):
    Avg= (Game1+Game2+Game3)/3
    Handicap= (Basis -230)*0.90
    Basis= Avg - Handicap
    return Avg,Handicap,Basis

LastName= input("Enter the bowler's last name")
Game1= int(input("Enter the score for game 1"))
Game2= int(input("Enter the score for game 2"))
Game3= int(input("Enter the score for game 3"))

Basis= 0
Handicap= 0
Avg,Handicap,Basis= AverageScore(Game1,Game2,Game3,Basis,Handicap)

print("The bowler's last name is",LastName)
print("The bowler's average score is",Avg)
print("The bowler's average score with handicap is",Handicap)