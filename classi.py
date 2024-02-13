class ClasseMadre: 
    def __init__(self,input): 
        self.input_numerico = input
        
    def stampa_messaggio(self): 
        print(f"Classe madre: input numerico - {self.input_numerico}")
        if self.input_numerico == 1: 
            print('''la seonda classe chiede due credenziali in input
                  nome : user   pass : 1234''')  
    
class Secondo_Oggetto(): 
    def __init__(self):
        self.nome = ''
        self.password = ''
        
    def chiedi_credenziali(self):
        self.nome = input("Inserisci il nome: ") 
        self.password = input("Inserisci la password: ")
        
    def sovrascrivi_credenziali(self): 
        self.nome = input("Inserisci il nuovo nome: ") 
        self.password = input("Inserisci la nuova password: ") 
    
    def conferma_input(self): 
        conferma = input("Conferma (1) o errore (0): ") 
        try:
            if conferma == "1":
                print('confermato')
                return True   
            elif conferma == "0":
                return self.sovrascrivi_credenziali()
        except ValueError:
            print('errore inserisci 1 or 0')
    
class TerzoOggetto: 
    def __init__(self): 
        self.nome = secondo_oggetto.nome
        self.password = secondo_oggetto.password
    def stampa_dati(self):
        print(f"Nome: {self.nome} - Password: {self.password}")
      
    def esegui(self):
        secondo_oggetto.chiedi_credenziali() 
        self.stampa_dati() 
        if secondo_oggetto.conferma_input(): 
            print("Programma chiuso.") 
        else: 
            nuovo_terzo_oggetto = TerzoOggetto() 
            nuovo_terzo_oggetto.esegui()
    
# Creazione delle istanze 
classe_madre = ClasseMadre(1) 
classe_madre.stampa_messaggio() 
secondo_oggetto = Secondo_Oggetto()
terzo_oggetto = TerzoOggetto()
terzo_oggetto.stampa_dati()
terzo_oggetto.esegui()