import random

parc_solaire = {
    "nom": "DeepTech Maurice - Nord",
    "puissance_theorique": 20.0,
    "prix_kwh": 0.18,
    "historique": [],
    "maintenace_hebdo": 5.0
}

for i in range(7):
    facteur_meteo = random.uniform(0.75, 1.0)
    prod_du_jour = parc_solaire["puissance_theorique"] * facteur_meteo
    parc_solaire["historique"].append(prod_du_jour)

total_prod = sum(parc_solaire["historique"])
gain_total = total_prod * parc_solaire["prix_kwh"]
benefice_net = gain_total - parc_solaire["maintenace_hebdo"]

print(f"--- Rapport : {parc_solaire['nom']} ---")
print(f"Production totale : {total_prod:.2f} kWh")
print(f"Revenu généré : {gain_total:.2f} €")
print(f"Bénéfice net : {benefice_net:.2f} €")

