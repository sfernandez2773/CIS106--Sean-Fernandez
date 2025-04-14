def DisplayNames(Names, ExamScores):
    for i in range(len(Names)):
        print(f"{Names[i]}: {ExamScores[i]}")

Names= ["Luna", "Esme", "Halo", "LunaSnow", "Sue", "Wanda", "Stephen", "Klay", "Draymond"]
ExamScores= [100, 90, 95, 85, 80, 75, 70, 65, 60]
DisplayNames(Names, ExamScores)
