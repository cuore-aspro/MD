def numero():
    x = float(input("Inserisci un numero: "))
    return x

def luca ():
    
    while True:

        x = numero()
        try:                # try: esegue il codice
            if x < 0:
                raise Exception("Variable x è minore di zero") # raise: genera un errore
                
        except NameError:   # except: se c'è un errore esegue il codice
            print("la variabile x non è stata definita")
    
        except ValueError:  # except: se c'è un errore esegue il codice
            if not isinstance(x, int or float):
                print('x is not a number')
        
        else :              # else: se non c'è nessun errore esegue il codice
            if x < 10:
                print('Value is less than 10')
    
        finally:            # finally: esegue il codice in ogni caso
            print(f"you insert number: {x}")
            break
            
luca()
        


x = -1 
