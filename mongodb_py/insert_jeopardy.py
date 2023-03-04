from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
from bson import ObjectId
import json

load_dotenv(find_dotenv())
printer = pprint.PrettyPrinter()

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://learning:{password}@learning.ayz3ibh.mongodb.net/?retryWrites=true&w=majority&authSource=admin"
client = MongoClient(connection_string)

sample_data = client.sample_data
jeopardy_question = sample_data.jeopardy_question

insert_bulk = []
f = open("JEOPARDY_QUESTIONS1.json")
data = json.load(f)

for d in data:
    insert_bulk.append(d)
    
jeopardy_question.insert_many(insert_bulk)


