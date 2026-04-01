def creer_parc():
    nom = input("Entrez le nom du parc : ")
    puissance = float(input("Entrez la puissance du parc : "))
    prix = float(input("prix kWh : "))
    maintenance = float(input("Coût de maintenance : "))
    return {"nom": nom, "puissance": puissance, "prix": prix, "maintenance": maintenance}

ma_flotte = []

print(" --- Création de la première flotte --- ")
ma_flotte.append(creer_parc())

print(" --- Création de la deuxième flotte --- ")
ma_flotte.append(creer_parc())

print(" --- Création de la troisième flotte --- ")
ma_flotte.append(creer_parc())

print("\n--- Récapitulatif de la flotte ---")
for parc in ma_flotte:
    print(f"Parc détecté : {parc['nom']}")
