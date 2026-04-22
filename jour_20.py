import json

ma_flotte = [
    {"nom": "Alpha", "puissance": 1000, "prix" : 0.20, "maintenance" : 50},
    {"nom": "Beta", "puissance": 5000, "prix" : 0.15, "maintenance" : 200},
    {"nom": "Gamma", "puissance": 2000, "prix" : 0.10, "maintenance" : 300},
    {"nom": "Delta", "puissance": 500, "prix" : 0.25, "maintenance" : 20},
    {"nom": "Epsilon", "puissance": 3000, "prix" : 0.18, "maintenance" : 150},
]

with open("flotte_sauvegardee.json", "w") as f:
    json.dump(ma_flotte, f)

with open("flotte_sauvegardee.json", "r") as f:
    ma_flotte_chargee = json.load(f)

print(f"Données récupérées : {ma_flotte_chargee}")
