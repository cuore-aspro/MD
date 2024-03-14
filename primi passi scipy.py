import numpy as np
from scipy.optimize import minimize,root
from scipy.integrate import odeint
from scipy.interpolate import interp1d
from scipy.fft import fft ,ifft,fftfreq
from scipy.linalg import solve,eig
from scipy.stats import norm
import matplotlib.pyplot as plt
from scipy import integrate




# OTTIMAZZIONE
'result = minimize(funzione_da_ottimizzare,valori iniziali)'
def objective(x):
    return (x[0] - 2) ** 2 + (x[1] - 3) ** 2
# Initial guess
x0 = [0, 0]
# Minimize the objective function
result = minimize(objective, x0)
print(result)
print("")


# INTEGRAZIONE
'integral, errore = intergrate.quad(funzione_da_integrare,limite_inferiore,limite_max)'
def f(x):
    return x ** 2
# Calcola l'integrale definito di f da 0 a 1
result, error = integrate.quad(f, 0, 1)
print("Risultato:", result)
print("Errore stimato:", error)
print("")


# INTERPOLAZIONE
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 2, 4, 6, 8, 10])
# Create an interpolation function
f = interp1d(x, y)
# Generate new x values
new_x = np.linspace(0, 5, num=11)
# Interpolate y values for the new x values
new_y = f(new_x)
print("Interpolated values:", new_y) 
print("")


# TRASFORMATA D FOURIER 
'trasformata = fft(dati)'
# Generate a signal
t = np.linspace(0, 1, num=1000)
signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 10 * t)
# Compute the FFT
freqs = fftfreq(len(signal))
fft_vals = fft(signal)
# Plot the frequency spectrum
plt.plot(freqs, np.abs(fft_vals))
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.show()
print("")


# ALGEBRA LINEARE: (Ax = b) dove b = vettore ,A = matrice ,la funzione solve restituisce il vettore (x) ,
# la funzione (eig) usata anche per trovare gli autovalori e gli auto vettori di una matrice
a = np.array([2,3][4,1])
b = np.array([5,6])
soluzione = solve(a,b)
print("")


# statistiche funzionali : genera valori casuali dalla distribuzione normale(o gaussiana)
# l funzione (rvs) dal modulo (norm) genera valori random e size = numero valori
val = norm.rvs(size=5)
print("")


# Risoluzione di equazioni differenziali ordinarie (scipy.integrate.odeint):
# Derivata della variabile y rispetto ad x
def derivative(y, x):
    return -2 * y
# Condizione iniziale
y0 = 1.0
x = np.linspace(0, 5, num=100)
# Risoluzione dell'equazione differenziale
y = odeint(derivative, y0, x)
# Plot
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()



# Calcolo degli zeri di una funzione (scipy.optimize.root)
# Definizione della funzione
def equation(x):
    return x**3 + 2*x - 5
# Trova lo zero della funzione
result = root(equation, x0=0)
print("Risultato:", result.x)
print("")