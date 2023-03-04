import pyarrow
from pymongoarrow.api import Schema
from pymongoarrow.monkey import patch_all
import pymongoarrow as pma
from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime as dt

load_dotenv(find_dotenv())
printer = pprint.PrettyPrinter()

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://learning:{password}@learning.ayz3ibh.mongodb.net/?retryWrites=true&w=majority&authSource=admin"
client = MongoClient(connection_string)
 
production = client.production
person_collection = production.person_collection

patch_all()

author = Schema({"_id":ObjectId, 
                 "first_name":pyarrow.string(),
                 "last_name":pyarrow.string(),
                 "date_of_bith": dt})

df = production.author.find_pandas_all({}, schema = author)
arrow_table = production.author.find_arrow_all({}, schema = author)
ndarrays = production.author.find_numpy_all({}, schema = author)


print(df)
print(arrow_table)
print(ndarrays)