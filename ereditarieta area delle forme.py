from abc import ABC, abstractmethod
import math


class Forme(ABC):
    @abstractmethod
    def __init__ (self):
        raise NotImplementedError("Devi implementare il metodo __init__")
    @abstractmethod
    def area(self):
        raise NotImplementedError("Devi implementare il metodo area") 
    
class Cerchio(Forme):
     
    def __init__(self,raggio):
        super().__init__()
        self.raggio = raggio
    
    def area(self):
        return  math.pi * self.raggio **2
    
class Rettangolo(Forme):
    
    def __init__(self,base,altezza):
        super().__init__()
        self.base = base
        self.altezza = altezza
        
    def area (self):
        return self.base * self.altezza
    
class Triangle(Forme):
    
    def __init__(self,base,altezza):
        super().__init__()
        self.base = base
        self.altezza = altezza
    
    def area (self):
        return (self.base * self.altezza) / 2  

class Quadrato(Forme):
    
    def __init__(self,lato):
        super().__init__()
        self.lato = lato
    
    def area(self):
        return self.lato **2

cerchio = Cerchio(5)
print(f'l\'area del cerchio e di : {cerchio.area()} cm2')
print("")

rettangolo = Rettangolo(5,10)
print(f'l\'area del rettangolo è di : {rettangolo.area()} cm2')
print("")

triangolo = Triangle(5,10)
print(f'l\'area del triangolo è di : {triangolo.area()} cm2')
