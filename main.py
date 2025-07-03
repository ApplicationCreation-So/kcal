import streamlit as st
import pandas as pd
import os

FICHIER_ALIMENTS = "aliments.csv"

df_aliments = pd.read_csv(FICHIER_ALIMENTS)

st.title("🍽️ Suivi Nutritionnel")

# =========================
# 🧮 Formulaire de recherche
# =========================
st.header("🧮 Calculer les macros")

# 🔍 Barre de recherche
recherche = st.text_input("🔎 Rechercher un aliment :").lower()

# Filtrer la liste
aliments_disponibles = df_aliments[df_aliments["nom"].str.lower().str.contains(recherche)]["nom"].tolist()

if not aliments_disponibles:
    st.warning("Aucun aliment trouvé.")
    st.stop()

# Sélecteur d’aliment (filtré)
aliment = st.selectbox("Choisir un aliment :", aliments_disponibles)
poids = st.number_input("Quantité en grammes :", min_value=0.0, step=10.0)

if st.button("Ajouter"):
    data = df_aliments[df_aliments["nom"] == aliment].iloc[0]
    facteur = poids / 100
    kcal = round(data["kcal"] * facteur, 1)
    glucides = round(data["glucides"] * facteur, 1)
    lipides = round(data["lipides"] * facteur, 1)
    proteines = round(data["protéines"] * facteur, 1)

    st.subheader("📊 Résultat")
    st.markdown(f"""
    **{poids}g de {aliment} contient :**
    - 🔸 {kcal} kcal  
    - 🟢 {glucides} g glucides  
    - 🔵 {lipides} g lipides  
    - 🟣 {proteines} g protéines  
    """)

