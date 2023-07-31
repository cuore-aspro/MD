from abc import ABC , abstractclassmethod


class Capo():
    @abstractclassmethod
    def __init__(self):
        pass
    def saluto(self):
        pass
    
class Casa(Capo):
    def __init__(self,casa ):
        super().__init__()
        self.casa = casa
    def saluto(self):
        print(f'questa {self.casa} è di una puttana')
        
class Auto(Capo):
    def __init__(self,auto):
        super().__init__()
        self.auto = auto
    def saluto(self):
        print(f'questa {self.auto} è di una puttana')
        
class Nome(Capo):
    def __init__(self,nome):
        super().__init__()
        self.__nome = nome
    def saluto(self):
        print(f'ciao sono {self.__nome} è sono una puttana')

macchina = Auto('ferrari')
macchina.saluto()
nome = Nome('Marta')
nome.saluto()
casa = Casa('Villa')
casa.saluto()