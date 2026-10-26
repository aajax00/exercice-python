poids = float(input("Entrer votre poids en kg: "))
taille = float(input("Entrer votre taille en m: "))

if taille > 0:
    imc = poids / (taille ** 2)
    print(f"Votre IMC est: {imc:.2f}")
else:
    print("ERREUR: la taille être strictement positive")
