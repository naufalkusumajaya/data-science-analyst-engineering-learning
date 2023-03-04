from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
from bson import ObjectId
import datetime

load_dotenv(find_dotenv())
printer = pprint.PrettyPrinter()

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://learning:{password}@learning.ayz3ibh.mongodb.net/?retryWrites=true&w=majority&authSource=admin"
client = MongoClient(connection_string)

sample_data = client.sample_data
jeopardy_question = sample_data.jeopardy_question

def fuzzy_matching():
    result = jeopardy_question.aggregate([
        {
            "$search":{
                "index": "language_search",
                "text": {
                    "query":"computer",
                    "path": "category",
                    "fuzzy":{}
                }
            }
        }
    ])
    printer.pprint(list(result))

def synonyms_find():
#     {
#   "analyzer": "lucene.english",
#   "searchAnalyzer": "lucene.english",
#   "mappings": {
#     "dynamic": true
#   },
#   "synonyms": [
#     {
#       "analyzer": "lucene.english",
#       "name": "mapping",
#       "source": {
#         "collection": "synonyms"
#       }
#     }
#   ]
# }
    result = jeopardy_question.aggregate([
        {
            "$search":{
                "index": "language_search",
                "text": {
                    "query":"car",
                    "path": "category",
                    "synonyms": "mapping"
                }
            }
        }
    ])
    printer.pprint(list(result))
    
def autocomplete():
    result = jeopardy_question.aggregate([
        {
            "$search":{
                "index": "language_search",
                "autocomplete":{
                    "query": "what is love",
                    "path": "question",
                    "tokenOrder": "sequential",
                    "fuzzy" : {}
                }
            }
        },
        {    
            "$project":{
                "_id":0,
                "question":1
            }
        }
    ])
    printer.pprint(list(result))
    
def compound_q():
    result = jeopardy_question.aggregate([
        {
            "$search": {
                "index":"language_search",
                "compound":{
                    "must": [
                        {
                            "text": {
                                "query":["COMPUTER", "CODING"],
                                "path": "category"
                            }
                        }
                    ],
                    "mustNot": [
                        {
                            "text": {
                                "query":"codes",
                                "path": "category"
                            }
                        }
                    ],
                    "should": [
                        {
                            "text": {
                                "query":"application",
                                "path": "answer"
                            }
                        }
                    ]
                }
            }        
        },
        {
            "$project":{
                "_id":0,
                "question":1,
                "category":1,
                "answer":1,
                "score":{"$meta":"searchScore"}
            }
        }
    ])
    printer.pprint(list(result))

def relevance_score():
    result = jeopardy_question.aggregate([
        {
            "$search": {
                "index":"language_search",
                "compound":{
                    "must": [
                        {
                            "text": {
                                "query":"geography",
                                "path": "category"
                            }
                        }
                    ],
                    "should": [
                        {
                            "text": {
                                "query":"Final Jeopardy",
                                "path": "round",
                                "score": {"boost": {"value":3.0}}
                            }
                        },
                        {
                            "text": {
                                "query":"Double Jeopardy",
                                "path": "round",
                                "score": {"boost": {"value":2.0}}
                            }
                        }
                    ]
                }
            }        
        },
        {
            "$project":{
                "_id":0,
                "question":1,
                "category":1,
                "answer":1,
                "round":1,
                "score":{"$meta":"searchScore"}
            }
        },
        {
            "$limit":100
        }
    ])
    printer.pprint(list(result))
    
relevance_score()