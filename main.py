import streamlit as st
import pandas as pd

# ---- Base d'aliments ----
aliments = {
    "Pomme": {"kcal": 52, "glucides": 14, "lipides": 0.2, "protéines": 0.3},
    "Poulet rôti": {"kcal": 165, "glucides": 0, "lipides": 3.6, "protéines": 31},
    "Riz cuit": {"kcal": 130, "glucides": 28, "lipides": 0.3, "protéines": 2.7},
    "Avocat": {"kcal": 160, "glucides": 8.5, "lipides": 15, "protéines": 2}
}

st.title("🧮 Compteur de Macros")

aliment = st.selectbox("Choisir un aliment :", list(aliments.keys()))
poids = st.number_input("Quantité en grammes :", min_value=0.0, step=10.0)

if st.button("Ajouter"):
    data = aliments[aliment]
    facteur = poids / 100

    result = {
        "kcal": round(data["kcal"] * facteur, 1),
        "glucides": round(data["glucides"] * facteur, 1),
        "lipides": round(data["lipides"] * facteur, 1),
        "protéines": round(data["protéines"] * facteur, 1)
    }

    st.subheader("🔍 Résultat")
    st.write(f"**{poids}g de {aliment} contient :**")
    st.write(f"• 🟠 {result['kcal']} kcal")
    st.write(f"• 🟢 {result['glucides']} g de glucides")
    st.write(f"• 🔵 {result['lipides']} g de lipides")
    st.write(f"• 🟣 {result['protéines']} g de protéines")
