import pandas as pd
import os 

def load_and_validate_file(uploaded_file, reference_columns, save_path="data/new_data.csv"):
    """
    Charge un fichier CSV, vérifie ses colonnes et enregistre s'il est valide.
    """
    try:
        # Charger les données
        df = pd.read_csv(uploaded_file)

        # Vérifier les colonnes
        if list(df.columns) != reference_columns:
            raise ValueError(
                f"Les colonnes du fichier ne correspondent pas.\n"
                f"Colonnes attendues : {reference_columns}\n"
                f"Colonnes reçues : {list(df.columns)}"
            )
        
        # Convertir les colonnes numériques (avec gestion des erreurs)
        numeric_columns = [
            'Order Value', 'Delivery Fee', 'Discounts and Offers',
            'Commission Fee', 'Payment Processing Fee', 'Refunds/Chargebacks'
        ]
        for col in numeric_columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')  # Remplace les non-numériques par NaN

        # Enregistrer le fichier validé
        if not os.path.exists("data"):
            os.makedirs("data")
        df.to_csv(save_path, index=False)
        
        return df, None

    except Exception as e:
        return None, str(e)
