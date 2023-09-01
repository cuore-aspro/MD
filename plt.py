import matplotlib.pyplot as plt
import pandas as pd
import numpy as np






x = np.array([23,33,22,34,55]) 
y = np.array([6,7,11,9,30]) 

plt.scatter(x,y)
plt.title('grafico casuale')

plt.xlabel('anni')
plt.ylabel('sperienza')

plt.show()
