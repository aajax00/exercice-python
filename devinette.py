import random

reponse = random.randint(1, 100)
essai = 0

while essai != reponse:
    essai = int(input("Devinez le nombre entre 1 et 100: "))
    
    if essai < reponse:
        print("Plus grand")
    
    elif essai > reponse:
        print("Plus petit")
    
    else:
        print(f"Félicitations! Vous avez trouvé le nombre {reponse} avec l'essais {essai}.")
    
    