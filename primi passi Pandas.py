
import pandas as pd
import numpy as np


# Creazione di una serie
serie = pd.Series([np.arange(0, 10)])
print(serie)

# Esercizio 1# Analisi delle vendite di un negozio: hai un dataframe con le seguenti colonne:# data, prodotto, quantita, prezzo unitario
data = {'Data': ['2023-01-02', '2023-01-02', '2023-01-03', '2023-01-03', '2023-01-04'],
        'prodotto': ['penna', 'matita', 'gomma', 'astuccio', 'quaderno'], 
        'quantita': [10, 20, 15, 5, 10], 
        'prezzo_unitario': [1.2, 0.8, 1.2, 0.8, 1.2]}
vendite = pd.DataFrame(data)

vendite['fatturato'] = vendite['quantita'] * vendite['prezzo_unitario'] #creo una nuova colonna fatturato
fatturato_prodotto = vendite.groupby('prodotto')['fatturato'].sum()    #raggruppo per prodotto e sommo il fatturato al gruppo prodotto
print(f'Fatturato totale per prodotto:\n{fatturato_prodotto}\n')

# Prodotto più venduto in termini di quantità
prodotto_piu_venduto = vendite.groupby('prodotto')['quantita'].sum().idxmax() #raggruppo per prodotto e sommo la quantita' al gruppo prodotto e trovo l'indice del valore massimo
print(f'Prodotto più venduto:\n{prodotto_piu_venduto}\n')

# Creiamo un nuovo dataframe con le vendite mensili
vendite['Data'] = pd.to_datetime(vendite['Data']) #trasformo la colonna data in formato datetime
fatturato_mensile = vendite.groupby(vendite['Data'].dt.to_period('M'))['fatturato'].sum() #raggruppo per mese e sommo il fatturato con il metodo dt.to_period('M')
print(f'Fatturato mensile:\n{fatturato_mensile}\n')