import pandas as pd
import pymongo
import tkinter as tk
from tkinter import messagebox

class Registro:
    def __init__(self):
        self.registro = pd.DataFrame(columns=['nome', 'cognome', 'data di nascita', 'citta', 'email', 'telefono', 'patrimonio'])

    def aggiungi_persona(self, nome, cognome, data_di_nascita, citta, email, telefono, patrimonio):
        nuovo = pd.DataFrame({'nome': [nome], 'cognome': [cognome], 'data di nascita': [data_di_nascita], 'citta': [citta], 
                              'email': [email], 'telefono': [telefono],'patrimonio':[patrimonio]})
        self.registro = pd.concat([self.registro, nuovo], ignore_index=True)
        return self.registro

    def salva_su_mongodb(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["il_tuo_database"]
        collection = db["la_tua_collezione"]
        records = self.registro.to_dict(orient='records')
        collection.insert_many(records)
        client.close()

class RegistroGUI:
    def __init__(self, root, registro):
        self.root = root
        self.root.title("Aggiungi Persona")
        self.registro = registro
        
        self.nome_label = tk.Label(root, text="Nome:")
        self.nome_label.pack()
        self.nome_entry = tk.Entry(root)
        self.nome_entry.pack()
        
        self.cognome_label = tk.Label(root, text="Cognome:")
        self.cognome_label.pack()
        self.cognome_entry = tk.Entry(root)
        self.cognome_entry.pack()
        
        # Aggiungi altre entry per gli altri campi
        
        self.aggiungi_button = tk.Button(root, text="Aggiungi Persona", command=self.aggiungi_persona)
        self.aggiungi_button.pack()
    
    def aggiungi_persona(self):
        nome = self.nome_entry.get()
        cognome = self.cognome_entry.get()
        # Ottieni i valori dalle altre entry
        
        # Aggiungi persona al registro
        self.registro.aggiungi_persona(nome, cognome, ...)
        messagebox.showinfo("Successo", "Persona aggiunta con successo al registro.")
        
        # Salvare su MongoDB
        self.registro.salva_su_mongodb()
        
        # Resetta le entry dopo l'aggiunta
        self.nome_entry.delete(0, tk.END)
        self.cognome_entry.delete(0, tk.END)
        # Resetta le altre entry

# Creare un'istanza della classe Registro
registro = Registro()

# Creare una finestra Tkinter
root = tk.Tk()

# Creare un'istanza della classe RegistroGUI e passare la finestra Tkinter e il registro come argomenti
registro_gui = RegistroGUI(root, registro)

registro = Registro()
registro.aggiungi_persona('Mario', 'Rossi', '12/12/1990', 'Roma', 'rossi@gmail.com',34040,1200)
registro.aggiungi_persona('Luigi', 'Verdi', '12/12/1980', 'Roma', 'luigi@gmail.com',12345,4500)
registro.aggiungi_persona('andrea', 'Rossi', '12/12/1970', 'Roma', 'rossi@gmail.com',34040,600)
registro.aggiungi_persona('Luca', 'Verdi', '12/12/2000', 'Roma', 'luigi@gmail.com',12345,60455)
registro.aggiungi_persona('dario', 'Rossi', '12/12/1999', 'Roma', 'rossi@gmail.com',34040,5644)
registro.aggiungi_persona('giulio', 'Verdi', '12/12/2015', 'Roma', 'luigi@gmail.com',1234,53456)
registro.aggiungi_persona('paolo', 'Rossi', '12/12/2050', 'Roma', 'rossi@gmail.com',34040,4563)
registro.aggiungi_persona('gigi', 'Verdi', '12/12/2030', 'Roma', 'luigi@gmail.com',12345,34564)

# Avviare il loop principale
root.mainloop()
    
    
    
    
    