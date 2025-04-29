import pymongo

url = 'mongodb+srv://kmnaveen777:naveen@atlas.eokhe.mongodb.net/'

client = pymongo.MongoClient(url)
db = client['test_mongo']  # Replace with your actual database name in Atlas
