import pandas as pd
from datetime import datetime, timedelta
import random
import os


# Funktion zum Generieren zufälliger Verkaufsdaten
def generate_random_sales_data(num_records_inner):
    # Zufällige Produkte und Preise definieren
    products = ['Product A', 'Product B', 'Product C', 'Product D']
    prices = {'Product A': 20.0, 'Product B': 15.0, 'Product C': 30.0, 'Product D': 25.0}

    # Startdatum festlegen
    start_date = datetime(2024, 1, 1, 8)  # 1. Januar 2024 um 8 Uhr

    data = []

    for _ in range(num_records_inner):
        date = start_date + timedelta(
            minutes=random.randint(0, 1440 * 30))  # Zufälliger Zeitpunkt innerhalb eines Monats
        transaction_id = random.randint(1, num_records_inner // 10)
        product = random.choice(products)
        quantity = random.randint(1, 5)
        sales = prices[product] * quantity
        data.append([date, transaction_id, product, quantity, sales])

    return pd.DataFrame(data, columns=['date', 'transaction_id', 'product', 'quantity', 'sales'])


# Anzahl der zu generierenden Datensätze
num_records = 500

# Generieren der Daten
sales_data = generate_random_sales_data(num_records)

# Verzeichnis erstellen, falls es nicht existiert
os.makedirs('data', exist_ok=True)

# Speichern der Daten als CSV-Datei
sales_data.to_csv('data/sales_data.csv', index=False)

print("CSV-Datei mit Verkaufsdaten wurde erfolgreich erstellt.")
