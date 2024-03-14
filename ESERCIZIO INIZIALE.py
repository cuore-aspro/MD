from scipy import integrate
from scipy import optimize
import numpy as np

'''ESERCIZIO 1'''
# utilizza scipy per calcolar l'integrale numerica
'''dati : 
funzione: f(x)=e-x2
intervallo: da 0 a 1 '''

def funct(x):
    return np.exp(-x**2)

integral ,error = integrate.quad (funct,0,1)
print(f'integrale = {integral}\t errore = {error}')



'''ESERCIZO 2'''
# utilizzare scipy per rivolvere l'equzione differenziale 
'''dati :
(???? = -2?dtdy  = 2y) con la condizione iniziale( ?(0)=1y(0)=1 con l'intervallo da 0 a 5 '''
#funzione che presenta l'equazione
#dy/dt = 2y

def equazione(y,t):
    return -2*y

#condizione iniziale 
y0 = 1 #creazione intervall da 0 a 1 
t = np.linspace(0,5,100) #da 0 a 5 suddiviso in 100 punti
#risoluzione equazione differenziale 
soluzione = integrate.odeint(equazione,y0,t)

#preparazione oer la visulaizzazione dei dati 
result = np.column_stack(soluzione)
print(result)



'''ESERCIZIO 3'''
# ulitizza scipy per trovare il minim0 locale della funzione f(x)=x\4-x\2+2 ulizzando un metodo di ottimiazione
'''dati:
funzione: f(x)=x:4-x:2+2'''

def funzione(x):
    return x**4-x**2+2

risultato = optimize.minimize(funzione,x0=0)
print(risultato)