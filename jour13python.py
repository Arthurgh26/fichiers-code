parc_A = {}

nom_parc_A = input("Entrez le nom du premier parc : ")
puissance_parc_A = input("Quelle est sa puissance maximale en kWh ? ")
prix_de_vente = input("Quel est le prix de vente du kWh ? ")

parc_A["nom"] = nom_parc_A
parc_A["puissance"] = float(puissance_parc_A)
parc_A["prix_de_vente"] = float(prix_de_vente)

revenus_parc_A = parc_A["puissance"] * parc_A["prix_de_vente"]

print(f"--- Parc enregistré : {parc_A['nom']} ---")
print(f"Puissance configurée : {parc_A['puissance']} kwh")
print(f"Prix de vente du kwh : {parc_A['prix_de_vente']:.2f} €")
print(f"Revenus maximum possibles pour le {parc_A['nom']} : {revenus_parc_A:.2f} €")

parc_B = {}

nom_parc_B = input("Entrez le nom du second parc : ")
puissance_parc_B = input("Quelle est sa puissance maximale en kWh ? ")
prix_de_vente = input("Quel est le prix de vente du kWh ? ")

parc_B["nom"] = nom_parc_B
parc_B["puissance"] = float(puissance_parc_B)
parc_B["prix_de_vente"] = float(prix_de_vente)

revenus_parc_B = parc_B["puissance"] * parc_B["prix_de_vente"]

print(f"--- Parc enregistré : {parc_B['nom']} ---")
print(f"Puissance configurée : {parc_B['puissance']} kwh")
print(f"Prix de vente du kwh : {parc_B['prix_de_vente']:.2f} €")
print(f"Revenus maximum possibles pour le {parc_B['nom']} : {revenus_parc_B:.2f} €")

if revenus_parc_A > revenus_parc_B:
    print(f"Le parc {parc_A['nom']} est plus rentable.")
elif revenus_parc_B > revenus_parc_A:
    print(f"Le parc {parc_B['nom']} est plus rentable.")
else:
    print("Les deux parcs ont la même rentabilité.")



