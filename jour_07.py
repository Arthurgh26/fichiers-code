productions = [10.2, 15.5, 8.0, 12.4, 14.8, 7.2, 11.0]
prix_kwh = 0.22
gain_total = 0.0

print("--- Rapport financier hebdomadaire ---")

for p in productions:
    gain_jour = p * prix_kwh
    gain_total = gain_total + gain_jour

    if p > 14:
        statut = "EXCELLENT"
    elif p > 10:
        statut = "CORRECT"
    else:
        statut = "FAIBLE"

    print(f"Prod: {p:>4.1f} kWh | Gain: {gain_jour:.2f} € | {statut}")

print("-" * 40)
print(f"Recettes totale de la semaine : {gain_total:.2f} €")

gain_moyen = sum(productions) * prix_kwh / len(productions)
print(f"Gain moyen par jour : {gain_moyen:.2f} €")

          