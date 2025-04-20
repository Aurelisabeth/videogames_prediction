import streamlit as st
import pandas as pd
import pickle

# -------------------------
# 📦 Chargement du bundle
# -------------------------
with open("rf_bundle.pkl", "rb") as f:
    bundle = pickle.load(f)

model = bundle["model"]
genre_encoder = bundle["genre_encoder"]
platform_encoder = bundle["platform_encoder"]

# -------------------------
# 🧠 Options depuis les encodeurs
# -------------------------
genre_options = list(genre_encoder.classes_)
platform_options = list(platform_encoder.classes_)

# -------------------------
# 🎨 Mise en page Streamlit
# -------------------------
st.set_page_config(page_title="🎮 Prédire un best-seller", page_icon="🕹️")

st.title("🕹️ Prédiction de best-seller jeu vidéo")
st.markdown("Estimez si un jeu peut dépasser **1 million de ventes** avec l’aide d’un modèle IA.")

st.markdown("---")
st.header("📋 Données du jeu")

# Champs utilisateurs
genre = st.selectbox("🎮 Genre du jeu", options=genre_options)
platform = st.selectbox("🖥️ Plateforme", options=platform_options)
year = st.slider("📅 Année de sortie", min_value=1980, max_value=2025, value=2020)

# Encodage utilisateur
genre_encoded = genre_encoder.transform([genre])[0]
platform_encoded = platform_encoder.transform([platform])[0]

X_input = pd.DataFrame([{
    'Platform_enc': platform_encoded,
    'Year': year,
    'Genre_enc': genre_encoded
}])

# -------------------------
# 🔍 Prédiction automatique
# -------------------------
st.markdown("---")
st.header("🎯 Résultat de la prédiction")

prediction = model.predict(X_input)[0]

if prediction == 1:
    st.success("✅ Ce jeu a de **bonnes chances de devenir un best-seller** (≥ 1 million de ventes) !")
else:
    st.warning("❌ Ce jeu a **peu de chances** d’atteindre le million.")

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center;'>Réalisé par Aurélie PERNELLE | Avril 2025</p>", unsafe_allow_html=True)
