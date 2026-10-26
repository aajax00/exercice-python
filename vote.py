nom = input("Entrer votre nom: ")
age = int(input("Entrer votre âge: "))

if age >= 18:
    print(f"{nom}, Vous pouvez voter")
    
else: 
    print("Vous n'êtes pas éligible pour voter")