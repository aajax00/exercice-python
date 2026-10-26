import getpass

mdp = getpass.getpass("Definissez votre mot de passe: ")
saisie = ""

while saisie != mdp:
    saisie = getpass.getpass("Saisissez le bon mot de passe: ")
    if saisie != mdp:
        print("Mot de passe incorrect. Veuillez réessayer.")
        
print("Mot de passe correct. Accès autorisé.")