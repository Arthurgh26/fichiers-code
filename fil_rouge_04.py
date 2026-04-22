def creer_parc():
    nom = input("Entrez le nom du parc : ")
    puissance = float(input("Entrez la puissance du parc : "))
    prix = float(input("prix kWh : "))
    maintenance = float(input("Coût de maintenance : "))
    benefice = puissance * prix - maintenance
    return {"nom": nom, "puissance": puissance, "prix": prix, "maintenance": maintenance, "benefice": benefice}

nombre_parcs = int(input("Combien de parcs voulez vous ajouter ?"))

ma_flotte = []

for i in range(nombre_parcs):
    print(f" --- Création de la flotte n°{i+1} --- ")
    ma_flotte.append(creer_parc())

def calcul_pi(parc):
    pi = (parc["benefice"]) / (parc["puissance"])
    return pi

for parc in ma_flotte:
    parc["performance_index"] = calcul_pi(parc)
    
somme_pi = sum(p["performance_index"] for p in ma_flotte)

moyenne_ile = somme_pi / nombre_parcs

ma_flotte.sort(key=lambda parc: parc["performance_index"])

parc_champion = ma_flotte[-1]
parc_critique = ma_flotte[0]

elite_flotte = []
zone_alerte = []

for parc in ma_flotte:
    if parc["performance_index"] >= moyenne_ile:
        elite_flotte.append(parc)
    else:
        zone_alerte.append(parc)


print(f"Le parc le plus efficace est {parc_champion["nom"]} avec un PI de {parc_champion["performance_index"]}")
print(f"Le parc le moins efficace est {parc_critique["nom"]} avec un PI de {parc_critique["performance_index"]}")

parcs_sup_moyenne = len(elite_flotte)
 
print(f"Le nombre de parc au dessus de la moyenne de l'ile est de {parcs_sup_moyenne}")