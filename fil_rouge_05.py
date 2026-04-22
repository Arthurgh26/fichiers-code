import json

def creer_parc():
    nom = input("Entrez le nom du parc : ")
    puissance = float(input("Entrez la puissnace du parc : "))
    prix = float(input("Entrez le prix du kwh : "))
    maintenance = float(input("Coût de maintenance : "))
    benefice = puissance * prix - maintenance
    return {"nom": nom, "puissance": puissance, "prix": prix, "maintenance": maintenance, "benefice": benefice}

def calcul_pi(parc):
    pi = (parc["benefice"]) / (parc["puissance"])
    return pi

try:
    with open("flotte_sauvegardee.json", "r") as f:
        ma_flotte = json.load(f)
        print("Donneées chargées avec succès !")
except FileNotFoundError:
    ma_flotte = []
    print("Aucune sauvegarde trouvée, nouvelle flotte crée.")

while True:
    print("\n--- MENU GESTION SOLAIRE MAURICE ---")
    choix = input("1. Ajouter un parc | 2. Diagnostique | 3. Quitter \n")
    if choix == "1":
        nouveau = creer_parc()
        ma_flotte.append(nouveau)
    elif choix == "2":
        if len(ma_flotte) > 0:
            for parc in ma_flotte:
                if "benefice" not in parc:
                    parc["benefice"] = (parc["puissance"] * parc["prix"] - parc["maintenance"])
            for parc in ma_flotte:
                parc["performance_index"] = calcul_pi(parc)
            somme_pi = sum(p["performance_index"] for p in ma_flotte)
            nombre_parcs = len(ma_flotte)
            moyenne_ile = somme_pi / nombre_parcs
            puissance_totale = sum(p["puissance"] for p in ma_flotte)
            benefice_total = sum(p["benefice"] for p in ma_flotte)
            if sum(p["maintenance"] for p in ma_flotte) > 0:
                roi = benefice_total / sum(p["maintenance"] for p in ma_flotte)
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
            noms_elite = [p["nom"] for p in elite_flotte]
            noms_alerte = [p["nom"] for p in zone_alerte]
            print(f"\n Il y a {nombre_parcs} parc")
            print(f"\n La moyenne de l'ile est de {moyenne_ile:.2f}")
            print(f"\n La puissance totale de l'ile est de {puissance_totale:.2f} kWh")
            print(f"\n Le benefice total de l'ile est de {benefice_total:.2f} euros")
            print(f"\n Le ROI global de l'ile est de {roi:.2f} euros")
            print(f"\n Le parc qui a le PI le plus élevé est le {parc_champion["nom"]}")
            print(f"\n Le parc qui a le PI le plus bas est le {parc_critique["nom"]}")
            print(f"\n Les parcs dont le PI est supérieur ou égal à la moyenne de l'ile sont {noms_elite}")
            print(f"\n Les parcs dont le PI est inférieur à la moyenne de l'ile sont {noms_alerte}")
        else:
            print("Aucun parc dans la flotte !")
    elif choix == "3":
        with open("flotte_sauvegardee.json", "w") as f:
            json.dump(ma_flotte, f)
            
        print("Sauvegarde effectueé. Au revoir !")
        break