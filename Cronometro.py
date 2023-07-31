#cronometro


import time

input = int(input('inserisci il tempo in secondi: '))
print(f'hai inserito {input} secondi')
print('')
print('il cronometro è partito')

def cronometro():
    global input
    while input > 0:
        print(f'{float(input)} secondi rimanenti')
        input -= 1
        time.sleep(1)
        if input == 0:
            print('il tempo è scaduto')
            break
cronometro()