from pandas import Series, DataFrame
import numpy as np

selection = Series([24,34,34,56,32,67,65,81,45,35,65,44],index=['gennaio','febraio','marzo','aprile','maggio','giugno',
'luglio','agosto','settembre','ottobre','novembre','dicembre'])
print(selection)

print('')
s1 = Series([3,5,7,9])
print(s1.prod()) # prodotto di tutti gli elementi
print('')
# DataFrame

vol = DataFrame(np.random.randn(9,4), index=['gennaio','febraio','marzo','aprile','maggio','giugno','luglio','agosto','settembre'],
columns=['temperatura','umidita','vento','pioggia'])
