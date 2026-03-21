import random

historique = []

for i in range(7):
    production_theorique = 15.0
    facteur_meteo = random.uniform(0.8, 1.0)
    production_reelle = production_theorique * facteur_meteo
    historique.append(production_reelle)

print(f"Historique de production sur 7 jours : {historique} kwh")

total_production_sur7 = sum(historique)
moyenne_production_sur7 = sum(historique) / len(historique)

if total_production_sur7 > 80:
    print("Semaine très rentable")

print(f"Moyenne de production sur 7 jours : {moyenne_production_sur7:.2f} kwh")