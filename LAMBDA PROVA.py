# import time 

# durata = float(input('inserisci il tempo in secondi: '))
# print(f'hai inserito {durata} secondi')
# print('')

# def cronometro():
#     global durata
    
#     while durata > 0:
#         print(f'{durata} secondi rimanenti')
#         durata -= 1
#         time.sleep(1)
#         if durata == 0:
#             print('tempo scaduto')
#             break
# cronometro()
# print('')


dati = lambda x: x**2                  #esempio con la funzione lambda
print(f'la funzione lambda da come risultato {dati(3)}')
print("")

lista = [1,2,3,4,5]
for i in range(len(lista)):            #esempio con il metoodo classico , cilco for
   lista[i] = lista[i]**2
print(lista)
print("")
my_list = [1,2,3,4,5]       #esempio con la funzione map iplementata con la funzione lambda
numeri_al_quadrato = list(map(lambda x: x**2, my_list))
print(f'la lista {my_list} al quadrato è {numeri_al_quadrato}')
print("")

get_first_item = lambda x: x[0]        #esempio con la funzione lambda che restituisce il primo elemento di una lista
print(f'la prima cifra\lettera della lista è: {get_first_item(my_list)}')
print("")

lista_personne = [('marco', 20), ('luca', 30), ('paolo', 40)]
lista_ordinata = sorted(lista_personne, key=lambda x: x[0])  #esempio con la funzione lambda che ordina una lista di tuple in base al primo elemento
lista_ordinata1 = sorted(lista_personne, key=lambda x: x[1]) #esempio con la funzione lambda che ordina una lista di tuple in base al secondo elemento
print(f'ecco la lista ordinata in base al primo elemento di ogni tupla prsente nella lista: {lista_ordinata} e questa è la lista ordinata in base al secondo elemento di ogni tupla presente nella lista: {lista_ordinata1}')
print('')

numeri = [1,2,3,4,5,6,7,8,9,10]                                #esempio con la funzione filter implementata con la funzione lambda
numeri_pari = list(filter(lambda x: x % 2 == 0,numeri))        #esempio con la funzione filter implementata per trovare i numeri pari
numeri_dispari = list(filter(lambda x: x % 2 != 0,numeri))     #esempio con la funzione filter implementata per trovare i numeri dispari
print(f'questa è la lista dei numeri pari: {numeri_pari} e questa è la lista dei numeri dispari: {numeri_dispari}')
print("")


from functools import partial           #esempio con la funzione partial

funzione = lambda x,y: x+y              #qui abbiamo la nostra funzione lambda      
somma = partial(funzione, 2)            #la funzione partial prende com primo argomento(x) con 2 e lo passa alla funzione lambda
print(somma(4))
print("")
#qui esegue la somma tra i due argomenti ed il secondo argomento(y) che è 4
#questo rende la nostra funzione più flessibile permettendoci di passare un argomento in un secondo momento che verrà sommato al primo argomento


#esempio con la funzione lambda in operazioni complesse

#esempio con la funzione lambda in un dizionario
dict = {'add': lambda x,y: x+y, 'sub': lambda x,y: x-y, 'mul': lambda x,y: x*y, 'div': lambda x,y: x/y} 

#utilizzando la funzione lambda in un dizionario possiamo creare una calcolatrice
somma = dict['add'](4,2)
sottrazione = dict['sub'](4,2)
moltiplicazione = dict['mul'](4,2)
divisione = dict['div'](6,3)






