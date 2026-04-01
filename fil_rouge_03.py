def creer_parc():
    nom = input("Entrez le nom du parc : ")
    puissance = float(input("Entrez la puissance du parc : "))
    prix = float(input("prix kWh : "))
    maintenance = float(input("Coût de maintenance : "))
    return {"nom": nom, "puissance": puissance, "prix": prix, "maintenance": maintenance}

nombre_parcs = int(input("Combien de parcs voulez vous ajouter ?"))

ma_flotte = []

for i in range(nombre_parcs):
    print(f" --- Création de la flotte n°{i+1} --- ")
    ma_flotte.append(creer_parc())

def analyser_parc(parc):
    benefice = (parc["puissance"] * parc["prix"]) - parc["maintenance"]
    return benefice

for parc in ma_flotte:
    benefice = analyser_parc(parc)
    if benefice >= 500:
        print(f"Le parc {parc['nom']} est rentable avec un bénéfice de {benefice:.2f} euros")
    else:
        print(f"Le parc {parc['nom']} n'est pas rentable avec un bénéfice de {benefice:.2f} euros")
benefice_total = sum(analyser_parc(parc) for parc in ma_flotte)

print(f"Le bénéfice total de la flotte est de {benefice_total:.2f} euros")

