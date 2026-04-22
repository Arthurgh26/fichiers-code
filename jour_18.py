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

nombre_parcs_puissants = 0

for parc in ma_flotte:
    if parc["puissance"] > 50000:
        nombre_parcs_puissants += 1


print(f"Le nombre de parc qui produisent plus de 50000 kWh est : {nombre_parcs_puissants}")
