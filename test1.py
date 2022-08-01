#Connecting pycharm with mongodb cloud

import pymongo
client = pymongo.MongoClient("mongodb+srv://datascience_ineuron:Reddy143@nikhil.bnsli.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    'name':'nikil',
    'email_id':'nikilmvr@gmail.com',
    'surname':'modusu'
}
db1 = client['test1']
coll = db1['test']
coll.insert_one(d)

