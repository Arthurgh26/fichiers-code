import pandas as pd

df = pd.read_csv("clients_sal.csv")

lignes_initiales = len(df)

print("=" * 50)
print("RAPPORT DE NETTOYAGE - DONNEES CLIENT PME")
print("=" * 50)
print(f"\nFichier chargé : {lignes_initiales} lignes détéctées.")

df = df.drop_duplicates(keep="first")

lignes_apres_doublons = len(df)
doublons_supprimes = lignes_initiales - lignes_apres_doublons

print(f"\n[DOUBLONS] {doublons_supprimes} ligne(s) en double spprimée(s).")

df["Date_facture"] = pd.to_datetime(
    df["Date_facture"],
    dayfirst=True,
    errors="coerce"
)

df["Date_facture"] = df["Date_facture"].dt.strftime("%d/%m/%Y")

print("\n[DATES] Toutes les dates uniformisées au format JJ/MM/AAAA.")

df["Montant_euros"] =(
    df["Montant_euros"]
    .astype(str)
    .str.replace(" ","", regex=False)
)
df["Montant_euros"] = pd.to_numeric(df["Montant_euros"], errors="coerce")

print("\n[MONTANTS] Espaces supprimés, conversion en nombre effectué.")

valeurs_manquantes = df.isna().sum()

print("\n[VALEURS MANQUANTES] Détéctées avant remplacement :")
for colonne, nombre in valeurs_manquantes.items():
    if nombre > 0:
        print(f" - {colonne} {nombre} cellule(s) vide(s)")

df["Statut_paiement"] = df["Statut_paiement"].fillna("Non renseigné")
df["Email"] = df["Email"].fillna("Non renseigné")
df["Date_facture"] = df["Date_facture"].fillna("Non renseigné")
df["Montant_euros"] = df["Montant_euros"].fillna("0")

print("\n[VALEURS MANQUANTES] Cellules vides remplacées par 'Non renseigné'.")

lignes_finales = len(df)

print("\n" + "=" * 50)
print("RESUME")
print("=" * 50)
print(f"Lignes au départ       : {lignes_initiales}")
print(f"Doublons supprimés     : {doublons_supprimes}")
print(f"Lignes après nettoyage : {lignes_finales}")
print("Fichier propre sauvegardé : clients_propres.csv")

df.to_csv("clients_propres.csv", index=False)
