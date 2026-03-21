def conversion_kwh(valeur_wh) :
    resultat = valeur_wh / 1000
    return resultat

production_matin = 4500
prod_kwh = conversion_kwh(production_matin)

print(f"La production est de {prod_kwh:.2f} kWh")

def calculer_gain(kwh, prix_kwh):
    gain = kwh * prix_kwh
    return gain

prix_kwh = 0.15
gain_matin = calculer_gain(prod_kwh, prix_kwh)

print(f"Le gain du matin est de {gain_matin:.2f} euros")