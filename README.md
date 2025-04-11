# 🎮 Prédire un best-seller jeu vidéo avec IA

Ce projet permet de prédire si un jeu vidéo a des chances de devenir un **best-seller (≥ 1 million de ventes)** à partir de son **genre**, de sa **plateforme**, et de son **année de sortie**.

L’application est disponible en ligne grâce à [Streamlit Cloud](https://streamlit.io/).

---

## 🧠 Objectif

> Permettre à un éditeur de jeux vidéo d'estimer rapidement si un nouveau jeu pourrait atteindre un seuil symbolique de ventes, grâce à un modèle d'apprentissage automatique.

---

## 🛠️ Fonctionnalités

- Interface Streamlit simple et fluide (aucun bouton à cliquer)
- Entrée des données utilisateur :
  - 🎮 **Genre** du jeu
  - 🖥️ **Plateforme**
  - 📅 **Année de sortie**
- Prédiction automatique affichée en direct
- Modèle IA : **Random Forest Classifier**

---

## 📦 Structure du projet

```bash
📁 mon_projet/
├── app.py                  # L’application Streamlit
├── rf_bundle.pkl           # Modèle IA + encodeurs (sérialisés avec pickle)
├── requirements.txt        # Dépendances pour le déploiement
└── README.md               # Ce fichier
