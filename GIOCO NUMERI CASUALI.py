import random

def lancio():
    numero = random.randint(1,6)
    return numero

def numeri_marco():
    return random.choice([1,3,5])
def numeri_matteo():
    return random.choice([2,4,6])
    
def partita ():
    punti_marco = 0
    punti_matteo = 0
    
    while punti_marco < 3 and punti_matteo < 3:
        if lancio() == numeri_marco:
            punti_marco += 1
            print(f'punti Macro = {punti_marco}')
        else :
            punti_matteo += 1
            print(f'punti Matteo = {punti_matteo}')
            
    if punti_marco == 3 :
        print(f'Congratulazione Marco hai il vinto il match con {punti_marco} punti!! punteggio Matteo = {punti_matteo}')
    else :
        print(f'Congratulazione Matteo hai il vinto il match con {punti_matteo} punti !! punteggio Marco = {punti_marco}')

partita()
        
