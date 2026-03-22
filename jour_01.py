tension = 24
intensite = 8.5
puissance = tension*intensite
print(f"La tension est de {tension} V")
print(f"L'intensite estde {intensite} A")
print(f"La puissance genere est de {puissance} Watts")
temps = 5
energie = puissance*temps
print(f"L'energie est de {energie} Wh")
nombrepanneau = 5
rendement = nombrepanneau*energie
print(f"La production de {nombrepanneau} panneaux est de {rendement} Wh")
production  = rendement*7
print(f"La production d'energie par semaine est de {production} Wh")