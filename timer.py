import time 

def timer (durata):
    print('il tempo e stato impostato per {} secondi.'.format(durata))
    time.sleep(durata)
    print('il tempo e scaduto')
durata = 10
timer(durata)
