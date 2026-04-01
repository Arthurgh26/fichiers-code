def creer_parc():
    nom = input("Entrez le nom du parc : ")
    puissance = float(input("Entrez la puissance du parc : "))
    prix = float(input("prix kWh : "))
    return {"nom": nom, "puissance": puissance, "prix": prix}

def calculer_revenu(parc):
    revenu = parc["puissance"] * parc["prix"] 
    return revenu

p1 = creer_parc()
p2 = creer_parc()

rev1 = calculer_revenu(p1)
rev2 = calculer_revenu(p2)

print(f"Le parc {p1['nom']} rapporte {rev1:.2f} euros")
print(f"Le parc {p2['nom']} rapporte {rev2:.2f} euros")