import pymongo
client = pymongo.MongoClient("mongodb+srv://datascience_mongoDB:mongodb123@nikil.v3whoz2.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['MYinfo']
collection = database['Table']

'''
record = collection.find()
for i in record:
    print(i)
'''
#Query inside mongodb
"""
record1 = collection.find({'Company name': 'iNeuron'})
for i in record1:
    print(i)
"""

#Trying to fetch the data of course offered greater than E
record2 = collection.find({'Course offered': {"$gt": "E"}})
for i in record2:
    print(i)