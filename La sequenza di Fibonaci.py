def fibonacci(n):
    if n <= 0:
        return "Inserisci un numero postivo."  # verifichiamonche sia positivo
    elif n == 1:                               # se n è 1 allora il primo numero della sequenza è 0
        return 0                               # se n è 2 allora il secondo numero della sequenza è 1
    elif n == 2:
        return 1
    else:                          #elif n > 2:# se n è maggiore di 2 allora calcoliamo il n-esimo numero della sequenza      
        a, b = 0, 1                            # a = 0 e b = 1 , assegniamo i primi due numeri della sequenza
        for _ in range(n - 2):                 # n - 2 perchè abbiamo già calcolato i primi due numeri
            a, b = b, a + b                    # a = b e b = a + b , python asegna il valore di 'b' a 'a' e il valore di 'a + b' a 'b'
        return b
while True:
    try:
        n = int(input("Inserisci un numero intero n: "))
        result = fibonacci(n)
        print(f"Il {n}-esimo numero nella sequenza di Fibnacci è: {result}")
    except ValueError:
        print("Inserisci un numero valido.")


#sequenza di fibonacci : 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610 ecc...