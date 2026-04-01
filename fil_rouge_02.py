def creer_parc():
    nom = input("Entrez le nom du parc : ")
    puissance = float(input("Entrez la puissance du parc : "))
    prix = float(input("prix kWh : "))
    maintenance = float(input("Coût de maintenance hebdomadaire : "))
    return {"nom": nom, "puissance": puissance, "prix": prix, "maintenance": maintenance}

parc_1 = creer_parc()

parc_2 = creer_parc()

def analyser_rentabilite(parc):
    benefices = parc["puissance"] * parc["prix"] - parc["maintenance"]

    if benefices >= 15:
        return benefices, f"Le parc {parc['nom']} est EXCELLENT."
    else:
        return benefices, f"Le parc {parc['nom']} est A AMELIORER."


argent_1, verdict_1 = analyser_rentabilite(parc_1)
argent_2, verdict_2 = analyser_rentabilite(parc_2)

if argent_1 > argent_2:
    print(f"Le parc {parc_1['nom']} est plus rentable que le parc {parc_2['nom']}.")
elif argent_2 > argent_1:
    print(f"Le parc {parc_2['nom']} est plus rentable que le parc {parc_1['nom']}.")

print(f" {verdict_1}")
print(f" {verdict_2}")