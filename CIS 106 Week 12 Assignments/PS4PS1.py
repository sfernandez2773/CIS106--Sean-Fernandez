def Display(PlayerNames, BattingAverages):
    print("Player Names and Batting Averages:")
    for name, avg in zip(PlayerNames, BattingAverages):
        print(f"{name}: {avg}")

PlayerNames = ["Ohtani", "Trout", "Betts", "Harper", "Bellinger", "Soto", "Tatis", "Suzuki", "Smith", "Griffey"]
BattingAverages = [0.250, 0.299, 0.400, 0.255, 0.259, 0.305, 0.290, 0.265, 0.277, 0.255]

Display(PlayerNames, BattingAverages)
PlayerNames, BattingAverages = zip(*sorted(zip(PlayerNames, BattingAverages)))

while True:
    last_name = input("Enter a player's last name: ").strip()
    if last_name.lower() == 'Exit':
        print("Exiting the program.")
        break
    elif last_name in PlayerNames:
        index = PlayerNames.index(last_name)
        print(f"{last_name} has a batting average of {BattingAverages[index]:.3f}.")
    else:
        print(f"{last_name} is not in the list of players.")

