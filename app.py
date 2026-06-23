import streamlit as st
import pandas as pd
import joblib

# Chargement du modèle
model = joblib.load("churn_model.pkl")
columns = joblib.load("model_columns.pkl")

st.set_page_config(page_title="Churn Predictor", page_icon="📡", layout="centered")

st.title("📡 Churn Predictor — Télécom")
st.markdown("Prédit la probabilité qu'un client résilie son abonnement.")
st.divider()

# ─── FORMULAIRE ───────────────────────────────────────
st.subheader("📋 Informations client")

col1, col2 = st.columns(2)

with col1:
    tenure = st.slider("Ancienneté (mois)", 0, 72, 12)
    monthly_charges = st.slider("Facture mensuelle ($)", 18, 120, 65)
    contract = st.selectbox("Type de contrat", ["Month-to-month", "One year", "Two year"])
    internet_service = st.selectbox("Internet", ["DSL", "Fiber optic", "No"])
    online_security = st.selectbox("Sécurité en ligne", ["Yes", "No", "No internet service"])

with col2:
    tech_support = st.selectbox("Support technique", ["Yes", "No", "No internet service"])
    payment_method = st.selectbox("Méthode de paiement", [
        "Electronic check", "Mailed check",
        "Bank transfer (automatic)", "Credit card (automatic)"
    ])
    senior_citizen = st.selectbox("Senior (65+)", ["No", "Yes"])
    partner = st.selectbox("En couple", ["Yes", "No"])
    dependents = st.selectbox("Personnes à charge", ["Yes", "No"])

st.divider()

# ─── PRÉDICTION ───────────────────────────────────────
if st.button("🔍 Prédire le risque de churn", use_container_width=True):

    # Encodage manuel
    input_data = {
        "gender": 0,
        "SeniorCitizen": 1 if senior_citizen == "Yes" else 0,
        "Partner": 1 if partner == "Yes" else 0,
        "Dependents": 1 if dependents == "Yes" else 0,
        "tenure": tenure,
        "PhoneService": 1,
        "MultipleLines": 0,
        "InternetService": {"DSL": 0, "Fiber optic": 1, "No": 2}[internet_service],
        "OnlineSecurity": {"No": 0, "No internet service": 1, "Yes": 2}[online_security],
        "OnlineBackup": 0,
        "DeviceProtection": 0,
        "TechSupport": {"No": 0, "No internet service": 1, "Yes": 2}[tech_support],
        "StreamingTV": 0,
        "StreamingMovies": 0,
        "Contract": {"Month-to-month": 0, "One year": 1, "Two year": 2}[contract],
        "PaperlessBilling": 1,
        "PaymentMethod": {
            "Bank transfer (automatic)": 0,
            "Credit card (automatic)": 1,
            "Electronic check": 2,
            "Mailed check": 3
        }[payment_method],
        "MonthlyCharges": monthly_charges,
        "TotalCharges": tenure * monthly_charges
    }

    input_df = pd.DataFrame([input_data])[columns]
    proba = model.predict_proba(input_df)[0][1]
    prediction = model.predict(input_df)[0]

    # Résultat
    st.subheader("📊 Résultat")

    if proba >= 0.7:
        st.error(f"🔴 Risque élevé de churn — {proba*100:.1f}%")
        st.markdown("**Recommandation :** Contacter ce client immédiatement avec une offre de fidélisation.")
    elif proba >= 0.4:
        st.warning(f"🟡 Risque modéré de churn — {proba*100:.1f}%")
        st.markdown("**Recommandation :** Surveiller ce client et proposer un upgrade de contrat.")
    else:
        st.success(f"🟢 Risque faible de churn — {proba*100:.1f}%")
        st.markdown("**Recommandation :** Client fidèle, pas d'action urgente nécessaire.")

    st.progress(proba)