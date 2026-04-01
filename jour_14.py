def creer_parc():
    nom = input("Entrez le nom du parc : ")
    puissance = float(input("Entrez la puissance du parc : "))
    prix = float(input("prix kWh : "))
    return {"nom": nom, "puissance": puissance, "prix": prix}

print("--- Configuration Parc 1 ---")
parc1 = creer_parc()

print("--- Configuration Parc 2 ---")
parc2 = creer_parc()

