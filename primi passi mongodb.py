from pymongo import MongoClient



client = MongoClient('mongodb://localhost:27017/')
db = client['prova-database']
collection = db['prova-collection']

doc = [{'name':'john','age':25,'surname':'doe',},{ 'name':'dave','age':21,'surname':'doe'},
       {'name':'bresh','age':14,'surname':'list'},{'name':'favj','age':54,'surname':'list'},
       {'name':'jane','age':18,'surname':'york'},{'name':'arme','age':34,'surname':'york'}] 

collection.insert_many(doc)

collection_name = db.list_collection_names() # lista delle collezioni,crea una lista con i nomi delle collezioni
for name in collection_name:
    print(name)
collection_stat = collection.stats # statistiche sulla collezione

#eta maggiore a 15
query = {'age':{'$gt':15}}
user_doc = collection.find(query)
for nomi in user_doc:
    print(f'nome:{nomi['nomi']} \neta: {nomi['age']}')

#aggiornare l'eta
input = input('insert your name: ')
query = {'name':input}
person = collection.find_one(query)
if person['age'] < 14:
    new_age = {'$set':{'age':15}}
    collection.update_one(query,new_age)

#eliminare quelli con piu di 40 anni 
query = {'age':{'$gt':40}}
collection.delete_many(query)

#conteggio documenti senza criterio
count = collection.count_documents({})

#contare i documenti con eta maggiore di 15
query = {'age':{'$gt':15}}
number = collection.count_documents(query)
#un'altra maniera di fare la stessa cosa
number = {'$match':{'age':{'$gt':15}}} #match = trova i documenti che soddisfano i criteri specificati
pipeline = [number,{'$count':'number'}] #count = conta i documenti 
result = collection.aggregate(pipeline) #aggregazione
if result.alive:  #alive = controlla se il cursore è aperto
    print(result.next())  #next = restituisce il prossimo documento nel cursore
else:
    print('nessun risultato trovato')
    



pipeline = [
    # Fase 1: Filtra i documenti che soddisfano una condizione
    {"$match": {"age": {"$gt": 18}}},

    # Fase 2: Raggruppa i documenti in base ad uno o più campi
    {"$group": {"_id": "$surname", "count": {"$sum": 1}}},

    # Fase 3: Ordina i risultati in base al conteggio in ordine discendente
    {"$sort": {"count": -1}}
]

result = collection.aggregate(pipeline)

for doc in result:
    print(doc)

'''Nell'esempio sopra, la pipeline di aggregazione è definita come una lista di dizionari in pipeline. 
Ogni dizionario rappresenta una fase dell'aggregazione.


Nel nostro esempio:

La fase 1 ($match) filtra i documenti che hanno un campo "age" con un valore maggiore di 18.

La fase 2 ($group) raggruppa i documenti in base al campo "surname" e calcola il conteggio di documenti per ciascun valore di "surname".

La fase 3 ($sort) ordina i risultati in base al conteggio in ordine discendente.


Infine, il metodo aggregate() viene chiamato sulla collezione specificata collection e 
viene restituito un cursore che può essere iterato per recuperare i risultati delle operazioni di aggregazione'''

pi = [{'$group':{'_id': None,'avg_age':{'$avg':'$age'}}},
      {'$match':{'avg_age':{'$gt':25}}},
      {'$sort':{'avg_age':1}},
      {'$limit':1}]
result = collection.aggregate(pi)
for doc in result:
    print(doc)
db.close() #chiusura della connessione


'''($$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$)
1-il segno del dollaro($) serve per far riferimento anche ai campi del documento stesso,
ad esempio per fare riferimento al campo "age" di un documento, possiamo usare "$age"

2-nelle operazioni di aggregazione e di aggiornamento come $group, $match, $sort, $set, $inc, ecc.

3-variabili di contesto come $$CURRENT, $$ROOT, $$DESCEND, $$PRUNE, ecc.

in breve il segno del dollaro viene utilizzato pernellepipeline di aggregazione, per fare riferimento ai campi del documento stesso, 
per specificare operatori di aggiornamento e per variabili di contesto.
sono una parte cruciale della sintassi di MongoDB e vengono utilizzati in molte operazioni e funzionalità del database'''
