def Display(Names,Score):
    print("Name\tScore")
    for i in range(len(Names)):
        print(f"{Names[i]}\t{Score[i]}")

for Score in range(0,101,10):
    Names= ["Luna", "Esme", "Halo", "LunaSnow", "Sue", "Wanda", "Stephen", "Klay", "Draymond"]
    Score= [100, 90, 95, 85, 80, 75, 70, 65, 60]
    Display(Names,Score)
    print("Scores for the names are displayed above.")