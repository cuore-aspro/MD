#qui definiamo le carraterische del libro
class Libro:
    def __init__(self,autore,titolo,anno_di_publicazione,prezzo):
        self.autore = autore
        self.titolo = titolo
        self.prezzo = prezzo
        self.anno_di_publicazione = anno_di_publicazione


# Path: LIBRERIA.py  la nostra libreia
class Libreria:
    def __init__(self):
        self.libri = []
    print("")
    def aggiungi_libro(self,libro):
        self.libri.append(libro)
        return self.libri
        
    def rimuovi_libro(self,titolo):
        for libro in self.libri:
            if libro.titolo == titolo:
                self.libri.remove(libro)
        print(f'la libreri contiene {len(self.libri)} libri')
    print("")
    def cerca(self,titolo):
        for libro in self.libri:
            if libro.titolo.lower() == titolo:
                return libro
        print(f'la libreria contiene {len(self.libri)} libri')
    print('')
    def mostra_libri(self):
        for libro in self.libri:
            print(f"{libro.autore}, {libro.titolo}, {libro.anno_di_publicazione}, {libro.prezzo}")
        print(f'la libreri contiene {len(self.libri)} libri')    

#qua abbiamo la classe libro e libreria di prova che verranno aggiunte alla libreria principale
libreria = Libreria()
libro1 = Libro("J.K. Rowling","Harry Potter e la pietra filosofale",1997,6.00)
libro2 = Libro("J.K. Rowling","Harry Potter e la camera dei segreti",1998,8.00)
libro3 = Libro("J.K. Rowling","Harry Potter e il prigioniero di Azkaban",1999,7.00)
libro4 = Libro("J.K. Rowling","Harry Potter e il calice di fuoco",2000,10.00)

libreria.aggiungi_libro(libro1)
libreria.aggiungi_libro(libro2)
libreria.aggiungi_libro(libro3)
libreria.aggiungi_libro(libro4)
print('')

def elaborazione():
    
    while True:
        print("1. aggiungi libro")
        print("2. Rimuovi libro")
        print("3. Cerca libro")
        print("4. Mostra libri")
        print("0. Esci")
        print('')
        scelta = int(input("Seleziona un opzione: "))
        if scelta == 0:
            print('grazie per aver usato il nostro programma')
            break

        elif scelta == 1:
            autore = input("Inserisci autore: ")
            titolo = input("Inserisci titolo: ")
            anno_di_publicazione = int(input("Inserisci anno di pubblicazione: "))
            prezzo = float(input("Inserisci prezzo: "))
            libro = Libro(autore,titolo,anno_di_publicazione,prezzo)
            libreria.aggiungi_libro(libro)
            
        elif scelta == 2:
            libreria.mostra_libri()
            input('inserisci pin per confermare: ')
            if input != '1234':
                break  
            titolo = input("Inserisci titolo: ")
            libreria.rimuovi_libro(titolo)
            
        elif scelta == 3:
            libreria.mostra_libri()
            titolo = input("Inserisci titolo: ")
            libro = libreria.cerca(titolo)
            print(f"{libro.autore}, {libro.titolo}, {libro.anno_di_publicazione}, {libro.prezzo}")
            
        elif scelta == 4:
            libreria.mostra_libri()
            
        else:
            print("Scelta non valida")
            
elaborazione()
print('')



                
                
                
                
                
                
                
