from pandas import Series, DataFrame
import pandas as pd
import random
import asyncio
import matplotlib.pyplot as plt
# data = {'nome': ['Mario', 'Luigi', 'Paolo', 'Giovanni', 'Giuseppe'],
#         'eta': [23, 45, 34, 56, 23],
#         'voto': [80, 70, 60, 90, 100]}
# df = DataFrame(data)

# df['voto_alto'] = df['voto'] > 80
# big_student = df.groupby('voto_alto')['nome'].sum()

# print(f'{df}\t', big_student)
# print('')

# data = {'nome':['aspirapolvere', 'lavatrice', 'frigorifero', 'forno', 'lavastoviglie', 'microonde'],
#          'quantita': [10, 20, 30, 40, 50, 60],
#          'prezzo': [100, 200, 300, 400, 500, 600],
#          'sconto percentuale': [10, 20, 30, 40, 50, 60]}
         
# data1 = DataFrame(data)
# data1['totale'] = data1['quantita'] * data1['prezzo']
# vendite_totali  = data1.groupby('prodotto')['totale'].sum()
# Totale = data1['totale'] - data1['sconto percentuale']
# data1['prezzo scontato']  = data1['prezzo'] - data1['sconto percentuale']
# gudagno_totale = data1['totale'].sum()
# data1 = data1.set_index('nome')
# print(f'{data1}\n',vendite_totali, '\n', Totale)

class Registro:
    def __init__(self):
        self.registro = pd.DataFrame(columns = ['nome', 'cognome', 'data di nascita', 'citta', 'email', 'telefono','patrimonio'])
    
    def aggiungi_persona(self, nome, cognome, data_di_nascita, citta, email, telefono, patrimonio):
        nuovo = pd.DataFrame({'nome': [nome], 'cognome': [cognome], 'data di nascita': [data_di_nascita], 'citta': [citta], 
                              'email': [email], 'telefono': [telefono],'patrimonio':[patrimonio]})#creo un nuovo dataframe con i dati inseriti
        self.registro = pd.concat([self.registro, nuovo], ignore_index = True)  #index True serve per non avere indici duplicati
        return self.registro                                                    #
                                                                                #pd.concat serve per unire due dataframe
    def vizualiare_registro(self):
        return self.registro
    
    def sicurezza(self):
        pin = input('Inserisci il pin: ')
        condizione = self.registro['codice'] == pin
        riga = self.registro[condizione]
        return riga
    
    def cancella_persona(self):
        cod = input('inserisci il tuo codice ')#altrimenti si può usare il metodo drop: self.registro.drop(index = 0)
        condizione = self.registro['codice'] == cod
        self.registro = self.registro.drop(self.registro[condizione].index)
        return self.registro
    
    def salva (self):
        richiesta = input('Vuoi salvare? SI per confermare NO per annullare: ')
        try:
            if richiesta == richiesta.lower() == 'si':
                return True
        except:
            return False
        finally:
            print('grazie ed arrivederci')

    def torna_alla_pagina_precedente(self):
        pass
    
    def badge(self):
        numero = sum(random.sample(range(1, 100), 10))
        self.registro['codice'] = numero
        badge = self.registro.groupby('nome')['codice'].sum()
        print(f'NOME E NUMERO DEL BADGE:\n{badge}')
    
    def visualizza(self):
        return self.registro.to_csv('Registro_mail.csv',index = False) #index = False serve per non avere indici nel file csv
        
    
    
    def patrimonio(self):
        saldo = self.registro.groupby('nome')['patrimonio'].sum()
        return saldo
        
        
    def detagli(self):
        totale = self.registro['patrimonio'].sum()
        print(f'Il patrimonio totale è di:{totale} euro')
        patrimonio  = self.registro.groupby('nomi')['patrimonio'].sum()
        print(f'Il patrimonio per cognome è:\n{patrimonio}')
    
    def grafico(self):
        self.registro['data di nascita'] = pd.to_datetime(self.registro['data di nascita'])#trasformo la colonna in formato data
        
        x = self.registro['nome']
        y = self.registro['data di nascita']
        a = self.registro['patrimonio']
        b = self.registro['patrimonio']
        
        plt.plot(x,y, label = 'anno di nascita',color ='blue')
        plt.plot(x,a, label = 'patrimonio', color = 'red')
        plt.plot(x,b, label = 'media patrimonio', color = 'green')
        plt.legend() #serve per mostrare la legenda la legenda e' un'etichetta che spiega il grafico
        plt.show()









registro = Registro()
registro.aggiungi_persona('Mario', 'Rossi', '12/12/1990', 'Roma', 'rossi@gmail.com',34040,1200)
registro.aggiungi_persona('Luigi', 'Verdi', '12/12/1980', 'Roma', 'luigi@gmail.com',12345,4500)
registro.aggiungi_persona('andrea', 'Rossi', '12/12/1970', 'Roma', 'rossi@gmail.com',34040,600)
registro.aggiungi_persona('Luca', 'Verdi', '12/12/2000', 'Roma', 'luigi@gmail.com',12345,60455)
registro.aggiungi_persona('dario', 'Rossi', '12/12/1999', 'Roma', 'rossi@gmail.com',34040,5644)
registro.aggiungi_persona('giulio', 'Verdi', '12/12/2015', 'Roma', 'luigi@gmail.com',1234,53456)
registro.aggiungi_persona('paolo', 'Rossi', '12/12/2050', 'Roma', 'rossi@gmail.com',34040,4563)
registro.aggiungi_persona('gigi', 'Verdi', '12/12/2030', 'Roma', 'luigi@gmail.com',12345,34564)

registro.grafico()    
    
    
    
    
    