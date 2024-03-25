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
    
db.close()

# e possibile usarr le query e le aggregazioni per trovare i dati che soddisfano i criteri specificati
