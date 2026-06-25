# 📡 Churn Predictor — Télécom

Application de machine learning qui prédit la probabilité qu'un client télécom résilie son abonnement, avec recommandations business automatiques.

🔗 **[Voir l'application en ligne](https://churn-predictor-dm4xkeajaymxt2kinyj8bq.streamlit.app/)**

---

## 🎯 Objectif du projet

Identifier en amont les clients à risque de churn pour permettre aux équipes commerciales d'agir avant la résiliation — réduire le taux de churn est un enjeu majeur pour les opérateurs télécom.

---

## 💡 Insights clés

- **Les contrats mensuels ont un taux de churn de 42%** contre 3% pour les contrats 2 ans
- **Les nouveaux clients (< 10 mois) sont les plus à risque** — pic de départ dans les premiers mois
- **TotalCharges, MonthlyCharges et Tenure** sont les 3 facteurs les plus prédictifs
- Le modèle atteint un **AUC de 0.833** — très bonne capacité de discrimination

---

## 🛠️ Stack technique

| Outil | Usage |
|---|---|
| Python / Pandas | Nettoyage et exploration des données |
| Scikit-learn | Entraînement des modèles ML |
| Logistic Regression | Modèle final (AUC 0.833) |
| Random Forest | Modèle comparatif (AUC 0.811) |
| Joblib | Sauvegarde du modèle |
| Streamlit | Application web déployée en ligne |

---

## 📁 Structure du projet

churn-predictor/

│

├── app.py                  # Application Streamlit

├── churn_model.pkl         # Modèle entraîné

├── model_columns.pkl       # Colonnes du modèle

├── requirements.txt        # Dépendances Python

└── README.md               # Documentation

---

## 📊 Fonctionnalités de l'app

- **Formulaire interactif** — saisie des caractéristiques client
- **Prédiction en temps réel** — probabilité de churn instantanée
- **Code couleur** — 🟢 Faible / 🟡 Modéré / 🔴 Élevé
- **Recommandation business** — action suggérée selon le niveau de risque

---

## 📈 Résultats du modèle

| Modèle | Accuracy | AUC |
|---|---|---|
| Logistic Regression | 79% | 0.833 |
| Random Forest | 78% | 0.811 |

---

## 🚀 Lancer le projet en local

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📂 Dataset

Source : [Telco Customer Churn — IBM](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) — Kaggle  
7 043 clients télécom avec caractéristiques d'abonnement et statut de churn.
