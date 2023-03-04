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
 
production = client.global_superstore
person_collection = production.returns

patch_all()

author = Schema({"_id":ObjectId, 
                'Returned':pyarrow.string(), 
                'Order ID':pyarrow.string(), 
                'Market':pyarrow.string()})

df = person_collection.find_pandas_all({"Order ID":"ID-2011-20989"}, schema = author)
# arrow_table = production.author.find_arrow_all({}, schema = author)
# ndarrays = production.author.find_numpy_all({}, schema = author)


print(df)
# print(arrow_table)
# print(ndarrays)