rubrica = {}

while True :
    
    scelta = input('vuoi inserire un numero nuovo!! si or no: ')
    if scelta.lower() == 'no':
        break
    numero = int(input('inserisci numero : '))
    nome = input('inserisci nome : ')
    
    for nome,numero in rubrica.items():
        if nome in rubrica:
            print('nome già esistente nella rubrica')
            break
        
    rubrica[nome] = numero
            
for nome,numero in rubrica.items():
    print(f"ecco i numeri presenti nella rubrica = Nome: {nome} \tNumero: {numero}")
print("")
print('Grazie ed arrivederci...')
