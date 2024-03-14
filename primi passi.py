'''le 4 principali operazioni con MongoDB sono:

create (creazione) = db.collection.insertOne() or db.collection.insertMany()
read (lettura) = db.collection.find() or db.collection.findOne()
update (aggiornamento) = db.collection.updateOne() or db.collection.updateMany()
delete (cancellazione) = db.collection.deleteOne() or db.collection.deleteMany()'''

'''le query sono  comandi descrittivi che vengono utilizzati per trovare i dati 
che soddisfano i criteri specificati (quelli visto in precedenza )'''

'''aggregazione = è un processo di elaborazione dei dati 
replication =  e un processo di duplicazione dei dati
'''
from pymongo import MongoClient

# Connessione al server MongoDB
db = MongoClient('localhost', 27017) 

# selezionare o creazione del database
collection = db['test-database']

# prima oprezione (crud) create 
# inserire un nuvo documento nella collezione 
Doe_doc = collection.insert_one({'name': 'John', 'surname': 'Doe', 'age': 25})

# seconda operazione (crud) read
# trovare un documento nella collezione
query = {'name': 'John'}
user_doc = collection.find_One(query)
print(user_doc)

# terza operazione (crud) update
# aggiornare un documento nella collezione
new_age = {'$set': {'age': 26}}
collection.update(query, new_age)

# quarta operazione (crud) delete
# cancellare un documento nella collezione
collection.delete_one(query)

# indicazione 
#crea un indice per il campo name per velocizzare le query
collection.create_index([('name')]) 

#aggregazione 
pipeline = [{'$group': {'_id': '$name', 'count': {'$sum': 1}}}]
rsult = collection.aggregate(pipeline)
for doc in result:
    print(doc)

# chiusura della connessione
chiusura = db.close()


