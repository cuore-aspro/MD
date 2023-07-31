from abc import ABC,abstractclassmethod

class Metodo(ABC):
    @abstractclassmethod
    def saluto (self):
        pass

class Moto(Metodo):
    def saluto (self):
        print('la moto sta accelerando')
        
class Auto(Metodo):
    def saluto(self):
        print('l\'auto sta frenando')

auto1 = Auto()
auto1.saluto()




class Bank:
    
    def __init__(self,saldo):
        self.__saldo = saldo
        
    def prelievo(self):
        importo = int(input('inserisci l\'importo: '))
        if self.__saldo > importo :
            print(f'hai prelevato {importo} euro')
            return self.__saldo - importo
        else :
            print('fondi insufficenti')
    
    def versamento(self):
        importo = int(input('inserisci importo: '))
        return (importo + self.__saldo)
    
    def saldo(self):
         return self.__saldo
     
cash = Bank(3000)
cash.prelievo()
cash.versamento()
cash.saldo()