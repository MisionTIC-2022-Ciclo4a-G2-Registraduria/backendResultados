import pymongo
import certifi

ca = certifi.where()
client = pymongo.MongoClient(
    "mongodb+srv://andres10cortes07:20012022...franklin@misiontic.8wmnvvk.mongodb.net/results_db?retryWrites=true&w=majority",
    tlsCAFile=ca
)
db = client.test
print(db)

data_base = client["results_db"]
print(data_base.list_collection_names())
collection = data_base.get_collection("vote")
print(collection.find())

