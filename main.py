import pandas as pd
import matplotlib.pyplot as plt

# Daten einlesen
data = pd.read_csv('data/sales_data.csv', parse_dates=['date'])

# Überblick über die Daten
print(data.head())

# Verkaufszahlen pro Produkt plotten
product_sales = data.groupby('product')['sales'].sum()
product_sales.plot(kind='bar')
plt.title('Verkaufszahlen pro Produkt')
plt.xlabel('Produkt')
plt.ylabel('Verkaufszahlen')
plt.show()

# Tagesumsätze plotten
daily_sales = data.set_index('date').resample('D')['sales'].sum()
daily_sales.plot(kind='line')
plt.title('Tägliche Verkaufszahlen')
plt.xlabel('Datum')
plt.ylabel('Verkaufszahlen')
plt.show()

# Top-5 Transaktionen nach Umsatz anzeigen
top_transactions = data.sort_values(by='sales', ascending=False).head(5)
print("Top-5 Transaktionen nach Umsatz:")
print(top_transactions)
