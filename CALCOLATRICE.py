import math
import time


def presentazione():
    print('Benvenuto nella calcolatrice')
    print('')
    print('scegli l\'espressione che desideri eseguire a seconda dei numeri corispettivi:')
    print('')
    print('1.somma \n2.sottrazione \n3.moltiplicazione \n4.divisione \n5.potenza \n6.radice quadrata ')
    print("")
    print("")
    
presentazione()


def somma():
    return sum(numeri1)

def sottrazione():
    return numeri1[0] - numeri1[1]

def moltiplicazione():
    totale = 1
    for i in numeri1:
        totale *= i
    return totale

def divisione():
    return numeri1[0] / numeri1[1]

def potenza():
    return math.pow(numeri1[0], numeri1[1])

def radice_quadrata():
    return math.sqrt(numeri1[0])

scelta = input('seleziona operazione: ') 
input_1 = input('inserisci i numeri separandoli dalla \',\': ')
numeri1 = [float(num) for num in input_1.split(',')]

def calcolatrice():
    # global numeri1
    
    while True:
        if scelta == '1':
            print('hai scelto somma')
            risultato = somma()
            print(f'risultato = {risultato} ')
            break

        elif scelta == '2':
            print('hai scelto sottrazione')
            risultato = sottrazione()
            print(f'risultato = {risultato} ')
            break

        elif scelta == '3':
            print('hai scelto moltiplicazione')
            risultato = moltiplicazione()
            print(f'risultato = {risultato} ')
            break

        elif scelta == '4':
            if numeri1[0] == 0:
                print('non puoi dividere per zero')
            else:
                print('hai scelto divisione')
                risultato = divisione()
                print(f'risultato = {risultato} ')
            break

        elif scelta == '5':
            print('hai scelto potenza')
            risultato = potenza(numeri1)
            print(f'risultato = {risultato} ')
            break

        elif scelta == '6':
            if numeri1[0] < 0:
                print('il numero radicando deve essere positivo')
            else:
                print('hai scelto radice quadrata')
                risultato = radice_quadrata()
                print(f'risultato = {risultato} ')
            break

        else:
            print('hai inserito un\'opzione non valida, riprova')
            
            
    print('')
    print('grazie per aver usato la calcolatrice')

    
while True:
    calcolatrice()
    break
    