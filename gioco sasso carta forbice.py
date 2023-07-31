import random


def mano1():
    return random.choice(['sasso','carta','forbici'])

def mano2():
    return random.choice(['sasso','carta','forbici'])

def partita():
    punti1 = 0
    punti2 = 0
    
    while punti1 < 3 and punti2 < 3:
        if mano1() == 'sasso' and mano2() == 'forbici':
            punti1 += 1
            print(f'punti1 = {punti1}')
        elif mano1() == 'forbici' and mano2() == 'carta':
            punti1 += 1
            print(f'punti1 = {punti1}')
        elif mano1() == 'carta' and mano2() == 'sasso':
            punti1 += 1
            print(f'punti1 = {punti1}')
        elif mano1() == mano2():
            print('pareggio')
        else:
            punti2 += 1
            print(f'punti2 = {punti2}')
            
    if punti1 == 3:
        print(f'Congratulazione giocatore 1 hai il vinto il match con {punti1} punti!! punteggio giocatore 2 = {punti2}')
    else:
        print(f'Congratulazione giocatore 2 hai il vinto il match con {punti2} punti!! punteggio giocatore 1 = {punti1}')

partita()