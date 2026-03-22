niveau_batterie = 7
seuil_max = 80
seuil_min = 10

print(f"Niveau actuel : {niveau_batterie}%")

if niveau_batterie > seuil_max:
    print("ALERTE : Batterie trop chargée ! Arrêt du système")
    print("Surplus renvoyé sur le réseau.")
elif niveau_batterie < seuil_min:
    print("Danger : Batterie critique")
else:
    print("Charge en cours...")
    print(f"Il rest {seuil_max - niveau_batterie}% avant seuil max.")
       