productions = [12.5, 14.2, 10.8, 15.1, 9.5, 13.8, 12.0]
seuil = 11.0
prix = 0.20

print("--- Rapport de rentabilité ---")

for p in productions:
    if p >= seuil:
        print(f"Production de {p:.2f} kWh : RENTABLE (Gain : {p * prix:.2f} €)")
    else:
        print(f"Production de {p:.2f} kWh : INSUFFISANTE ")