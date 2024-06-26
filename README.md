# VerkaufsAnalyse
Das Projekt "VerkaufsAnalyse" analysiert Verkaufsdaten eines Einzelhandelsgeschäfts. Es generiert zufällige Verkaufsdatensätze, speichert sie in einer CSV-Datei und bietet grundlegende Analysefunktionen. Ideal für Data Scientists und Data Analysts, um ihre Fähigkeiten in Datenanalyse und -visualisierung zu verbessern.

# VerkaufsAnalyse

## Projektbeschreibung

Das Projekt "VerkaufsAnalyse" ist darauf ausgerichtet, Verkaufsdaten eines Einzelhandelsgeschäfts zu analysieren. Es generiert eine große Menge zufälliger Verkaufsdatensätze, speichert diese in einer CSV-Datei und bietet grundlegende Analysefunktionen. Dieses Projekt ist ideal für Data Scientists und Data Analysts, die ihre Fähigkeiten in der Datenanalyse und -visualisierung verbessern möchten.

## Funktionen

- Generierung zufälliger Verkaufsdaten
- Speicherung der Daten in einer CSV-Datei
- Analyse und Visualisierung der Verkaufsdaten

## Installation

1. Klonen Sie das Repository:
    ```bash
    git clone https://github.com/FloZewi/VerkaufsAnalyse.git
    cd VerkaufsAnalyse
    ```

2. Erstellen Sie eine virtuelle Umgebung und aktivieren Sie sie:
    ```bash
    python -m venv env
    source env/bin/activate  # Auf Windows: env\Scripts\activate
    ```

3. Installieren Sie die benötigten Pakete:
    ```bash
    pip install pandas numpy matplotlib
    ```

## Verwendung

1. Führen Sie das Skript zur Generierung der Verkaufsdaten aus:
    ```bash
    python generate_sales_data.py
    ```

2. Das Skript erstellt eine CSV-Datei mit zufälligen Verkaufsdaten im Verzeichnis `data`:
    - `data/sales_data.csv`

3. Führen Sie das Hauptprogramm aus, um die Verkaufsdaten zu analysieren:
    ```bash
    python main.py
    ```

## Struktur

- `generate_sales_data.py`: Skript zur Generierung und Speicherung zufälliger Verkaufsdaten.
- `main.py`: Hauptprogramm zur Analyse und Visualisierung der Verkaufsdaten.
- `.gitignore`: Datei zum Ausschließen unnötiger Dateien aus dem Git-Repository.
- `README.md`: Dokumentation des Projekts.
