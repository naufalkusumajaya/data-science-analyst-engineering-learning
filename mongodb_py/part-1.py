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

production = client.production
person_collection = production.person_collection

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

def find_bambang():
    # select * from person_collection where first_name = "bambang"
    bambang = person_collection.find({"first_name":"bambang"})
    for b in enumerate(bambang):
        printer.pprint(b)
    
def count_all_people():
    count = person_collection.count_documents(filter={})
    print("Number of people is ",count)

def find_by_id(person_id):
    _id = ObjectId(person_id)
    person = person_collection.find_one({"_id":_id})
    printer.pprint(person)
    
def get_age_range(min,max):
    query = {
        "$and":[
                {"ages":{"$gte":min}},
                {"ages":{"$lte":max}}                
            ]            
        }
    people = person_collection.find(query).sort("ages")
    for p in people:
        printer.pprint(p)

def select_columns():
    col = {"_id":0,"first_name":1, "last_name": 1}
    people = person_collection.find({},col)
    
    for p in people:
        printer.pprint(p)

def update_person_one_by_id(person_id):
    _id = ObjectId(person_id)
    
    updates = {
        "$set": {"new_field":"This is the business we choosen","last_name":"Teamlo"},
        "$inc": {"ages":69},
        "$rename": {"first_name":"first"}
    }
    person_collection.update_one({"_id":_id}, updates)
    
def update_many_by_name(name):
    update = {
        "$set": {"first_name":"panji"}
    }
    person_collection.update_many({"last_name":name}, update)

def remove_field(person_id):
    _id = ObjectId(person_id)
    
    update = {
        "$unset":{"new_field":""}
    }
    
    person_collection.update_one({"_id":_id}, update)
    
def replace_one(person_id):
    _id = ObjectId(person_id)
    
    replace = {
        "first_name": "new fn",
        "last_name" : "new ln",
        "birth" : 2006
    }
    person_collection.replace_one({"_id":_id}, replace)
    
def delete_doc_by_id(person_id):
    _id = ObjectId(person_id)
    # person_collection.delete_many(filter=...)
    person_collection.delete_one({"_id":_id})

address = {
    "province":"Jawa Tengah",
    "city":"Semarang",
    "street":"Jalan - jalan"
}

def add_address_embed(person_id, address):
    _id = ObjectId(person_id)
    
    person_collection.update_one({"_id":_id}, {"$addToSet":{"address":address}})

def add_address_relationship(person_id, address):
    _id = ObjectId(person_id)
    
    address = address.copy()
    address["owner_id"] = _id
    
    address_collection = production.address
    
    address_collection.insert_one(address)

add_address_relationship("63eb1cb1f4976865842b4069", address)