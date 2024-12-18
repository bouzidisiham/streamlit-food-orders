import streamlit as st
import pandas as pd
from scripts.data_loader import load_and_validate_file
from scripts.visualizations import (
    plot_payment_methods, plot_orders_by_restaurant,
    plot_orders_over_time, plot_order_value_distribution,
    plot_delivery_fee_vs_order_value
)

# CSS pour ajuster les marges
st.markdown(
    """
    <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
            padding-left: 0rem;
            padding-right: 0rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Colonnes de référence
REFERENCE_COLUMNS = [
    "Order ID", "Customer ID", "Restaurant ID", "Order Date and Time",
    "Delivery Date and Time", "Order Value", "Delivery Fee", "Payment Method",
    "Discounts and Offers", "Commission Fee", "Payment Processing Fee", "Refunds/Chargebacks"
]

st.title("🍽 Tableau de Bord des Commandes de Restaurants")

# Importation du fichier
uploaded_file = st.file_uploader("Importez votre fichier CSV :", type=["csv"])

if uploaded_file is not None:
    # Charger et valider les données
    df, error = load_and_validate_file(uploaded_file, REFERENCE_COLUMNS)

    if error:
        st.error(f"❌ Erreur : {error}")
    else:
        st.success("✅ Fichier validé et enregistré avec succès !")

        # Conversion des dates
        df['Order Date and Time'] = pd.to_datetime(df['Order Date and Time'])
        df['Delivery Date and Time'] = pd.to_datetime(df['Delivery Date and Time'])
        df['Delivery Time (Minutes)'] = (df['Delivery Date and Time'] - df['Order Date and Time']).dt.total_seconds() / 60

        # KPIs Dynamiques
        st.subheader("📊 Indicateurs Clés")
        col1, col2, col3 = st.columns(3)
        col1.metric("Nombre Total de Commandes", len(df))
        col2.metric("Valeur Totale des Commandes (€)", f"{df['Order Value'].sum():,.2f}")
        col3.metric("Délai Moyen de Livraison (min)", f"{df['Delivery Time (Minutes)'].mean():.1f}")

        col4, col5, col6 = st.columns(3)
        col4.metric("Total des Frais de Livraison (€)", f"{df['Delivery Fee'].sum():,.2f}")
        col5.metric("Remises et Offres Totales (€)", f"{df['Discounts and Offers'].sum():,.2f}")
        col6.metric("Montant des Remboursements (€)", f"{df['Refunds/Chargebacks'].sum():,.2f}")

        # Graphiques
        st.subheader("📈 Visualisations")
        st.pyplot(plot_payment_methods(df))
        st.pyplot(plot_orders_by_restaurant(df))
        st.pyplot(plot_orders_over_time(df))
        st.pyplot(plot_order_value_distribution(df))
        st.pyplot(plot_delivery_fee_vs_order_value(df))
