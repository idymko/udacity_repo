import pandas as pd
import numpy as np

# Kreditdaten
kaufpreis = 533e3
eigenkapital = 150e3
nebenkosten = 71046 # kaufpreis*0.1
print(f"kaufpreis\t {kaufpreis}")
print(f"eigenkapital\t {eigenkapital}")
print(f"nebenkosten\t {nebenkosten}")

darlehen = (kaufpreis+nebenkosten-eigenkapital)
print(f"darlehen\t {darlehen}")
zinssatz = 0.0325  # 3% p.a.
anfangstilgung = 0.06  # 2% p.a.

# Annuität berechnen (Jahresrate)
jahresrate = darlehen * (zinssatz + anfangstilgung)
monatsrate = jahresrate / 12

daten = []
restschuld = darlehen

for monat in range(1, 30*12):
    # Zinsanteil (auf Restschuld)
    zinsen = restschuld * zinssatz / 12
    tilgung = monatsrate - zinsen
    restschuld -= tilgung
    
    daten.append({
        "Jahr": np.round(monat/12,2),
        "Rate (€)": round(monatsrate, 2),
        "Zinsen (€)": round(zinsen, 2),
        "Tilgung (€)": round(tilgung, 2),
        "Restschuld (€)": round(restschuld, 2)
    })
    
    if restschuld<0:
        break
    
df = pd.DataFrame(daten)
print(df)

print(f"\nzinsensumme\t {df['Zinsen (€)'].sum().round(0)}")