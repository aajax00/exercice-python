total_sec = int(input("Entrer le nombre de secondes: "))

heures = total_sec // 3600
reste_sec = total_sec % 3600

minutes = reste_sec // 60
secondes = reste_sec % 60

print(f"{heures} heures, {minutes} minutes et {secondes} secondes")