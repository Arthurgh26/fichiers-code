donnees_parc = [
    [12.5, 14.0, 10.2],
    [11.8, 15.2, 9.5]
]

print(f"Prod Panneau B / Jour 2 : {donnees_parc[1][1]} kWh")

total_A = 0

for production_jour in donnees_parc[0]:
    total_A = total_A + production_jour

print(f"Total panneau A : {total_A} kWh")

