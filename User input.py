import random
import time

def presentazione():
    print('Ciao, benvenuto nel programma di inserimento dati!')
    print('')
    nome = input('Inserisci il tuo ID: ')   # Aggiungere nome, cognome, età, sesso, data di nascita e luogo di nascita
    print('')
    print(f'Ciao {nome}, per accedere al programma di inserimento dati devi eseguire un esercizio di sicurezza.')
    print('')
    print('Ti sarà chiesto di svolgere degli esercizi per poi inserire il codice di sicurezza.')
    print('')
    print(f'Buona fortuna {nome}!')
    print('')
    print('Inserisci i tuoi dati.')
    nome_cognome = input('Inserisci il tuo nome e cognome: ')
    abitazione = input('Inserisci la tua abitazione: ')
    eta_sesso = input('Inserisci la tua età e il tuo sesso: ')
presentazione()

print('')
print('Hai 3 vite per svolgere gli esercizi e 20 secondi per ogni esercizio.')
print("")

def esercizio1():
    numero_primo = input('Inserisci un numero primo tra 20 e 30: ')
    print('')
    if numero_primo in ['23', '29']:
        print('Risposta corretta!')
    else:
        print('Risposta sbagliata.')
        raise Exception('Hai finito le vite.')

def esercizio2():
    print('1. Alessandro Manzoni e 1800 \n2. Giuseppe Verdi e 1700 \n3. Giuseppe Garibaldi e 1900 \n4. Leonardo Da Vinci e 1500')
    print('')
    cultura = input('Chi ha scritto il libro \'I Promessi Sposi\' e in che epoca fu ambientata? scrvi il nome o l\'anno')
    if cultura.lower() == 'alessandro manzoni' or cultura == '1800':
        print('Risposta corretta!')
    else:
        print('Risposta sbagliata.')
        raise Exception('Hai finito le vite.')

def esercizio3():
    capitali = input('Quali sono le capitali di questi differenti stati europei? \n1. Italia \n2. Francia \n3. Germania \n4. Spagna \n5. Inghilterra: ')
    print('')
    if capitali.lower() == 'roma,parigi,berlino,madrid,londra':
        print('Risposta corretta!')
    else:
        print('Risposta sbagliata.')
        raise Exception('Hai finito le vite.')

def esercizio4():
    inganno = input('Qual\'è il numero che da sempre lo stesso risultato sia nella moltiplicazione che nella somma? ')
    if inganno == '2':
        print('Risposta corretta!')
    else:
        print('Risposta sbagliata.')
        raise Exception('Hai finito le vite.')

def scelta_esercizio():
    esercizi = [esercizio1, esercizio2, esercizio3, esercizio4]
    random.shuffle(esercizi)

    for esercizio in esercizi:
        scelta = input('Premi ENTER per iniziare l\'esercizio.')
        print('')
        esercizio()
        print('')
        time.sleep(30)  # Tempo di pausa tra un esercizio e l'altro

try:
    for i in range(3):
        scelta_esercizio()
        print('Esercizio completato con successo!')
        print('')

    print('Hai completato gli esercizi con successo!')
except Exception as e:
    print(str(e))

chance = 3
while chance > 0:
    code = int(input('Inserisci il codice di sicurezza prima di procedere: '))
    print(f'Hai ancora {chance} tentativi per inserire il CODICE CORRETTO')
    if code == 1234:
        print('Hai inserito il codice giusto.')
        break
    else:
        chance -= 1
        if chance == 0:
            print('Hai finito i tentativi.')
            break

persona = {'nome': 'aimeric', 'eta': 25}

def start():
    operazioni = ('aggiungere', 'cancellare', 'modificare')
    print(operazioni)
    print('')
    operazione = input('Cosa vuoi fare? Scegli tra le differenti opzioni: ')

    if operazione == operazioni[0]:
        scelta = input('Aggiungi chiave:valore separati da una virgola: ')
        aggiungere(scelta.split(','))

    elif operazione == operazioni[1]:
        print('')
        scelta = input('Cancella chiave:valore separati da una virgola: ')
        cancellare(scelta.split(','))

    elif operazione == operazioni[2]:
        print('')
        while True:
            scelta = input('Modifica la chiave:valore accompagnata da una virgola: ')
            if not scelta.split(',')[0] in persona:
                break
            else:
                scelta = input('Modifica la chiave:valore separati da una virgola: ')
                modificare(scelta.split(','))

def aggiungere(param):
    chiave = param[0]
    valore = param[1]
    persona[chiave] = valore
    print(persona)

def cancellare(param):
    chiave = param[0]
    valore = param[1]
    persona.pop(chiave, valore)
    print(persona)

def modificare(param):
    chiave = param[0]
    valore = param[1]
    persona[chiave] = valore
    print(persona)
    


while True:
    start()
