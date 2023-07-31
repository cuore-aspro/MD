class Bancomat :
    def __init__(self,saldo_iniziale):
        self.__saldo_iniziale = saldo_iniziale
        
        
    def prelievo (self,importo):
        if self.__saldo_iniziale >= importo:
            self.__saldo_iniziale -= importo
            print(f'hai prelevato : {importo} euro ')
        else :
            print('Saldo insufficente!!! SEI POVERO')
    
    def carica_conto (self,importo):
        self.__saldo_iniziale += importo
        print (f'hai depositato {importo}')
    
    def saldo_finale(self):
        print('il tuo saldo finale è: ')
        return self.__saldo_iniziale
    
conto = Bancomat(2000)
conto.prelievo(600)
conto.carica_conto(3500)
print(conto.saldo_finale())

