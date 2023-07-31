class Bancomat :
    def __init__(self,saldo_iniziale):
        self.__saldo_iniziale = saldo_iniziale
        
    print('Benvenuto/a nella n ostra banca !!!')
    print("")
    print('come possiamo aiutarla?')

    print('PRELIEVO MAX GIORNALIERO : \n1000 EURO !!')
    print('')

    def prelievo (self):
        
        while True:
            max_prelivo_gionaliero = 1000
            Tax= 2
            scelta = input('vuoi effetuare un prelievo? si o no : ')
            if scelta.lower() == 'no':
                break
            
            importo = int(input('inserisci importo : '))
            print('')
            if importo < 20:
                print("non puoi prelevare meno di 20 euro !!!")
                break
            
            if self.__saldo_iniziale >= importo and importo < max_prelivo_gionaliero:
                self.__saldo_iniziale -= (importo + Tax)
                print('\t')
                print(f'hai prelevato : {importo} euro \t disponibilita {self.__saldo_iniziale}')
            
            elif importo > max_prelivo_gionaliero:
                print('non puoi prelevare piu di 1000 euro gionalieri')
                
    print('')       
    def versamento (self):
        while True:
            Tax = 1 
            scelta = input('vuoi effetuare un versamento? si o no : ')
            if scelta.lower() == 'no':
               break
           
            importo = int(input('inserisci importo : '))
            self.__saldo_iniziale += (importo - Tax)
            print(f'hai versato : {importo} euro')
            
    print('')       
    def saldo (self):
        print('saldo disponibile: ')
        return self.__saldo_iniziale

conto = Bancomat(3000)
conto.prelievo()
conto.versamento()
print(conto.saldo())

