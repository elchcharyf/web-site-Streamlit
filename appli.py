import streamlit as st 
import pickle
import numpy as np 

# Charger le modèle
with open("model.pkl","rb") as fille :
model = pickle.load(file)
# model = pickle.load(open('model.pkl', 'rb'))

st.title("Prédiction de l'attrition client")

st.sidebar.title("Menu de navigation")
st.sidebar.markdown("Bienvenue dans l'application de prédiction de l'attrition client. Utilisez le menu pour naviguer entre les différentes sections.")

# Champs de saisie utilisateur
credit_score = st.number_input("Credit Score", min_value=0)
age = st.number_input("Age", min_value=18, max_value=100)
tenure = st.number_input("Ancienneté (Tenure)", min_value=0, max_value=10)
balance = st.number_input("Solde (Balance)", min_value=0.0)
num_products = st.number_input("Nombre de produits", min_value=1, max_value=4)
has_cr_card = st.selectbox("Carte de crédit ?", ["Oui", "Non"])
is_active_member = st.selectbox("Membre actif ?", ["Oui", "Non"])
estimated_salary = st.number_input("Salaire estimé", min_value=0.0)

# Encodage des variables catégorielles
gender = st.selectbox("Genre", ["Homme", "Femme"])
geography = st.selectbox("Géographie", ["France", "Allemagne", "Espagne"])

# Conversion en variables numériques (One-hot encoding)
has_cr_card = 1 if has_cr_card == "Oui" else 0
is_active_member = 1 if is_active_member == "Oui" else 0
gender_female = 1 if gender == "Femme" else 0
gender_male = 1 if gender == "Homme" else 0
geo_france = 1 if geography == "France" else 0
geo_germany = 1 if geography == "Allemagne" else 0
geo_spain = 1 if geography == "Espagne" else 0

# Données au format attendu par le modèle
features = np.array([[credit_score, age, tenure, balance, num_products,
                      has_cr_card, is_active_member, estimated_salary,  # Exited is not needed as input
                      geo_france, geo_germany, geo_spain,
                      gender_female, gender_male]])
# Prédiction
if st.button("Prédire"):
    prediction = model.predict(features)
    st.write(f"Résultat de la prédiction : {'Client partira' if prediction[0] == 1 else 'Client restera'}")

