
#questa funzione verifca se un numero è primo
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


#un funzione che restituisce una lista di n numeri primi
def lista_numeri_primi(n):
    primi = []
    numero = 2
    while len(primi) < n:            #finchè la lunghezza della lista è minore di del valore di n allora continua ad aggiungere numeri primi alla lista
        if is_prime(numero):         #se e un nuemro primo lo aggiung alla lista
            primi.append(numero)
        numero += 1                  #incrementa il numero
    return primi


# chiede all'utente un numero intero n e stampa i primi n numeri primi
try:
    n = int(input("Inserisci un numero intero n: "))
    if n <= 0:
        print("Inserisci un numero positivo.")
    else:
        primi = lista_numeri_primi(n)
        print(f"I primi {n} numeri primi sono: {primi}")
except ValueError:
    print("Inserisci un numero valido.")
    print('')
finally:
    print(f'hai inserito: {n}')