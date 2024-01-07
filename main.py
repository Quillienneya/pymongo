from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

document = {'name': 'John Doe', 'age': 25}
collection.insert_one(document)

result = collection.find_one({'name': 'John Doe'})
print(result)
