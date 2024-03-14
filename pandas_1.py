import pandas as pd
from pandas import Series, DataFrame

#commandi piu' comuni per pandas

#creazione
pd.Series(data): #crea una serie
pd.DataFrame(data): #crea un dataframe
    
#lettura e scrttura
pd.read_csv('file.csv') #legge un file csv
pd.read_excel('file.xlsx') #legge un file excel
df.to_csv('file.csv') #scrive un file csv

#manipolazione
df.head(n) #mostra le prime 'n' righe
df.tail(n) #mostra le ultime 'n' righe
df.shape #mostra il numero di righe e colonne
df.describe() #mostra un riassunto statistico
df.sort_values(by='column') #ordina i valori del dataframe per colonna 

#selezione
df['column'].unique() #mostra i valori unici di una colonna
df['column'].iloc[0] #seleziona il primo valore della colonna
df['colum'] > 0 #seleziona i valori della colonna maggiori di 0
df['column'] #seleziona la colonna
df.loc[rows,column] #seleziona in base a righe e colonne
df.iloc[0] #seleziona la prima riga
df.iloc[0,0] #seleziona il primo valore della prima riga
df.iloc[row_index,column_index] #seleziona in base a indici di riga e colonna

#gestione dei valori mancanti
df.dropna() #rimuove le righe con valori mancanti
df.fillna(value) #sostituisce i valori mancanti con 'value'
df.isnull() #mostra i valori mancanti
df.isnull().sum() #mostra il numero di valori mancanti per colonna

#agregazione
df.groupby('column') #raggruppa i valori in base alla colonna
df.groupby('column').mean() #calcola la media per gruppo
df.groupby('column').sum() #calcola la somma per gruppo
df.groupby('column')['column'].sum() #calcola la somma per gruppo e colonna
df.sum() #calcola la somma per colonna o unisce le righe del dataframe
df.mean() #calcola la media per colonna
#trovare il valore massimo per ogni colonna
df.idmax() #trova il valore massimo per colonna
#merge and joint
pd.merge(df1,df2,on='column') #unisce due dataframe in base alla colonna
pd.concat([df1,df2]) #concatena due dataframe
pd.concat([df1,df2],axis=1) #concatena due dataframe per colonna
df1.append(df2) #concatena due dataframe