productions = [12.5, 14.2, 10.8, 15.1, 9.5, 13.8, 12.0]
jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

print(f"Productiondu lundi : {productions[0]} kWh")
print(f"Production du dimanche: {productions[6]} kWh")

total_semaine = sum(productions)
moyenne = total_semaine / len(productions)

print(f"Production totale de la semaine : {total_semaine:.2f} kWh")
print(f"Production moyenne quotidienne : {moyenne:.2f} kWh")

valeur_max = max(productions)
valeur_min = min(productions)

meilleur_jour = productions.index(valeur_max)
pire_jour = productions.index(valeur_min)


print(f"Meilleur jour de production : {jours[meilleur_jour]} il a produit {valeur_max:.2f} kWh")
print(f"Pire jour de production : {jours[pire_jour]} il a produit {valeur_min:.2f} kWh")
