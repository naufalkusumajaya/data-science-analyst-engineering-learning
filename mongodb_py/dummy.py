from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
from bson import ObjectId

load_dotenv(find_dotenv())
printer = pprint.PrettyPrinter()
password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://learning:{password}@learning.ayz3ibh.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)

#dbs = client.list_database_names()
test_db = client.test1
#collections = test_db.list_collection_names()

def insert_doc():
    collection = test_db.test1
    test_document = {
        "name":"Sri",
        "quote":"Ndang balio Sri"
    }
    uid = collection.insert_one(test_document).inserted_id
    print(uid)

production = client.global_superstore
person_collection = production.orders

def create_doc():
    first_name = ["bambang","paidi","barjo"]
    last_name = ["gendon","fuat"]
    ages = [1,2]
    
    # #cara 1 (kurang efisien)
    # for first_name, last_name, ages in zip(first_name,last_name,ages):
    #     doc = {"first_name":first_name, "last_name":last_name, "ages":ages}
    #     person_collection.insert_one(doc)
    
    # cara 2
    docs = []
    for first_name, last_name, ages in zip(first_name,last_name,ages):
        doc = {"first_name":first_name, "last_name":last_name, "ages":ages}
        docs.append(doc)
    
    print(docs)  
    # person_collection.insert_many(docs)
    
def find_all_people():
    people = person_collection.find()
    for p in people:
        printer.pprint(p)
        
find_all_people()