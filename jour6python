rendements = [95.2, 88.0, 45.5, 92.1, 30.2]
seuil_critique = 50.0

print("--- Rapport de rendement ---")

for r in rendements:
    if r < seuil_critique:
        print(f"Panneau à {r:.1f}% : Maintenance requise !!")
    elif r < 80.0:
        print(f"Panneau à {r:.1f}% : Nettoyage conseillé")
    else:    
        print(f"Panneau à {r:.1f}% : Fonctionnement optimal")

moyenne_parc = sum(rendements) / len(rendements)
print(f"\nEfficacité moyenne du parc : {moyenne_parc:.2f}%")

    

