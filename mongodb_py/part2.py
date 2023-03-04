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
 
production = client.production
person_collection = production.person_collection

def create_book_collection():
    books_validator = {
        "$jsonSchema":{
            "bsonType":"object",
            "required":["title","authors","publish_date","type","copies"],
            "properties":{
                "title":{
                    "bsonType": "string",
                    "description": "must be a string and is required"
                },
                "authors":{
                    "bsonType": "array",
                    "items":{
                        "bsonType":"objectId",
                        "description": "must be an objectId and is required"
                    }
                },
                "publish_date":{
                    "bsonType": "date",
                    "description": "must be a date and is required"
                },
                "type":{
                    "enum":["Fiction","Non-Fiction"],
                    "description": "can only from enum value and is required"
                },
                "copies":{
                    "bsonType": "int",
                    "minimum": 0,
                    "description": "must be an integer greater than 1 and is required"
                }
            }
        }
    }

    try:
        production.create_collection("book")
    except Exception as e:
        print(e)
        
    production.command("collMod","book",validator=books_validator)
    
def create_author_collection():
    author_validator = {
        "$jsonSchema": {
            "bsonType":"object",
            "required":["first_name","last_name","date_of_birth"],
            "properties":{
                "first_name":{
                    "bsonType": "string",
                    "description": "must be string and is required"
                },
                "string_name":{
                    "bsonType": "string",
                    "description": "must be string and is required"
                },
                "birth_of_date":{
                    "bsonType": "date",
                    "description": "must be date and is required"
                }
            }
        }
    }
    try:
        production.create_collection("author")
    except Exception as e:
        print(e)
        
    production.command("collMod","author",validator=author_validator)

def insert_bulk():
    
    authors = [
    {
        "first_name": "Miller",
        "last_name": "Justice",
        "date_of_birth": datetime.datetime(2017,10,19)
    },
    {
        "first_name": "Donaldson",
        "last_name": "Calderon",
        "date_of_birth": datetime.datetime(2021,1,14)
    }]
    
    author_collection = production.author
    authors = author_collection.insert_many(authors).inserted_ids
    
    books = [
    {
        "title": "Katherine Dotson",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7516
    },
    {
        "title": "Leona Bean",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6151
    },
    {
        "title": "Myrtle Moran",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2
    },
    {
        "title": "Lara Webb",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5150
    },
    {
        "title": "Hurley Sargent",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4027
    },
    {
        "title": "Sexton Mcguire",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2276
    },
    {
        "title": "Jennie Velazquez",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6922
    },
    {
        "title": "Lori Snyder",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7198
    },
    {
        "title": "Vickie Hoover",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2143
    },
    {
        "title": "Susanna Silva",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 560
    },
    {
        "title": "Janna Salazar",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6072
    },
    {
        "title": "Renee Rose",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8192
    },
    {
        "title": "Vazquez Rivas",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4464
    },
    {
        "title": "Luz Cobb",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9759
    },
    {
        "title": "Sybil Herman",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1361
    },
    {
        "title": "Small Peterson",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1427
    },
    {
        "title": "Russo Workman",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8939
    },
    {
        "title": "Salazar Bridges",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 393
    },
    {
        "title": "Perkins Stoday",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3750
    },
    {
        "title": "Sargent Hammond",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8948
    },
    {
        "title": "Cummings Lambert",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9450
    },
    {
        "title": "Ronda Gibson",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1574
    },
    {
        "title": "Mullen Bowers",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4920
    },
    {
        "title": "Rae Mccoy",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2152
    },
    {
        "title": "Norma Salinas",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3789
    },
    {
        "title": "Sheryl Daniels",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2537
    },
    {
        "title": "Chen Hutchinson",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1694
    },
    {
        "title": "Elsie Kim",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2831
    },
    {
        "title": "Mack Lancaster",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3382
    },
    {
        "title": "Stella Maddox",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9429
    },
    {
        "title": "Cherie Russo",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3353
    },
    {
        "title": "Dejesus Short",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4161
    },
    {
        "title": "Rojas Elliott",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8688
    },
    {
        "title": "Clay Obrien",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2749
    },
    {
        "title": "Michael Justice",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 455
    },
    {
        "title": "Valentine Nguyen",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8445
    },
    {
        "title": "Wiley Pitts",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6416
    },
    {
        "title": "Estelle Doyle",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5839
    },
    {
        "title": "Trujillo Underwood",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3614
    },
    {
        "title": "Elena Glenn",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4115
    },
    {
        "title": "Nona Barlow",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9872
    },
    {
        "title": "Craig Gilliam",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5450
    },
    {
        "title": "Karyn Butler",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3475
    },
    {
        "title": "Farley Cochran",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3396
    },
    {
        "title": "Huff Chen",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8658
    },
    {
        "title": "Laverne Holland",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5694
    },
    {
        "title": "Genevieve Winters",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4079
    },
    {
        "title": "Pearlie Navarro",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4944
    },
    {
        "title": "Laurel Carr",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5587
    },
    {
        "title": "Salas Manning",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5749
    },
    {
        "title": "Sanford Whitfield",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6540
    },
    {
        "title": "Avery Norton",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8277
    },
    {
        "title": "Meyer Reid",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2396
    },
    {
        "title": "Jane Edwards",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4238
    },
    {
        "title": "Celina Carpenter",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2779
    },
    {
        "title": "Rowland Mcmillan",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6458
    },
    {
        "title": "Nikki Trevino",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9415
    },
    {
        "title": "Yolanda Jackson",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6049
    },
    {
        "title": "Colon Espinoza",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 613
    },
    {
        "title": "Garza Morgan",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 426
    },
    {
        "title": "Dillard Merritt",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6567
    },
    {
        "title": "Edwina Hudson",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6718
    },
    {
        "title": "Stone Cain",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 600
    },
    {
        "title": "Long Benson",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9733
    },
    {
        "title": "Norris Stein",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5365
    },
    {
        "title": "Alexis Perez",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4793
    },
    {
        "title": "Eve Mccall",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5227
    },
    {
        "title": "Selma Johnston",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1416
    },
    {
        "title": "Fleming Larsen",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3509
    },
    {
        "title": "Shirley Morin",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6498
    },
    {
        "title": "Best Dickerson",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 826
    },
    {
        "title": "Daugherty Gilbert",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 340
    },
    {
        "title": "Blanche Guthrie",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 204
    },
    {
        "title": "Berg Sanford",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6026
    },
    {
        "title": "Estella Russell",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1634
    },
    {
        "title": "Madelyn Kennedy",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7398
    },
    {
        "title": "Flora Woods",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1685
    },
    {
        "title": "Rhodes Wilder",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9607
    },
    {
        "title": "Goff Mills",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2723
    },
    {
        "title": "Jodie Brock",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3526
    },
    {
        "title": "Alford Rice",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8636
    },
    {
        "title": "Sally Wooten",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3607
    },
    {
        "title": "Powers Booth",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 102
    },
    {
        "title": "Bradley Knapp",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9012
    },
    {
        "title": "Lang Bowman",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1129
    },
    {
        "title": "Mcgee Payne",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2947
    },
    {
        "title": "Walters Baxter",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3027
    },
    {
        "title": "Crystal Hood",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1510
    },
    {
        "title": "Hall Wright",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7237
    },
    {
        "title": "Myers Coffey",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6197
    },
    {
        "title": "Dominique Drake",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3957
    },
    {
        "title": "Tillman David",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8330
    },
    {
        "title": "Lelia Carlson",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8258
    },
    {
        "title": "Olive Chapman",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5665
    },
    {
        "title": "Harrell Cook",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7131
    },
    {
        "title": "Ora Dickson",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5244
    },
    {
        "title": "Jenna Watts",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6527
    },
    {
        "title": "Crawford Williams",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2968
    },
    {
        "title": "Livingston Gillespie",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5951
    },
    {
        "title": "Sellers Frank",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6634
    },
    {
        "title": "Adela Schmidt",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4775
    },
    {
        "title": "Garrison Cohen",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7935
    },
    {
        "title": "Billie Griffith",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4774
    },
    {
        "title": "Krystal Cross",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6281
    },
    {
        "title": "Lizzie Leblanc",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9635
    },
    {
        "title": "Jordan Sutton",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8416
    },
    {
        "title": "Winters Avila",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3324
    },
    {
        "title": "Elisa Ferguson",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7905
    },
    {
        "title": "Weber Wilkinson",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9582
    },
    {
        "title": "Gardner Ktodayles",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2458
    },
    {
        "title": "Gracie Ellison",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1686
    },
    {
        "title": "Poole Gallagher",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6134
    },
    {
        "title": "Whitfield Middleton",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 472
    },
    {
        "title": "Leonor Barrett",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8231
    },
    {
        "title": "Lenore Hernandez",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4293
    },
    {
        "title": "Lolita Emerson",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6932
    },
    {
        "title": "Cherry Cote",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5568
    },
    {
        "title": "Bush Nixon",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1471
    },
    {
        "title": "Bridgette Hampton",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3497
    },
    {
        "title": "Geneva Duncan",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2193
    },
    {
        "title": "Carly Combs",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8209
    },
    {
        "title": "Debra Sharp",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2851
    },
    {
        "title": "Addie Hays",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7280
    },
    {
        "title": "Mandy Sanders",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1069
    },
    {
        "title": "Lydia Cervantes",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4712
    },
    {
        "title": "Savannah Soto",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9042
    },
    {
        "title": "Judith Gomez",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1295
    },
    {
        "title": "Hahn Woodard",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1653
    },
    {
        "title": "Alyssa Santos",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5158
    },
    {
        "title": "Davidson Atkinson",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 812
    },
    {
        "title": "Sanchez Mendez",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7581
    },
    {
        "title": "Hardy Walsh",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3486
    },
    {
        "title": "Velez Richards",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1729
    },
    {
        "title": "Terrell Petty",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7579
    },
    {
        "title": "Beth Hunter",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9223
    },
    {
        "title": "Mona Day",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7249
    },
    {
        "title": "Humphrey Ballard",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6959
    },
    {
        "title": "Joyner Marsh",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2489
    },
    {
        "title": "Twila Gordon",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7998
    },
    {
        "title": "Candace Beach",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4643
    },
    {
        "title": "Walker Carson",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6917
    },
    {
        "title": "Courtney Rowe",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5738
    },
    {
        "title": "Sims Britt",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5153
    },
    {
        "title": "Marguerite Wheeler",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 99
    },
    {
        "title": "Gould Miller",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3485
    },
    {
        "title": "Parrish Fry",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3001
    },
    {
        "title": "Barron Mcclain",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4444
    },
    {
        "title": "Christy Moon",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9552
    },
    {
        "title": "Edith Jimenez",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4186
    },
    {
        "title": "Boyle Mercado",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3306
    },
    {
        "title": "Mayra Weeks",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9431
    },
    {
        "title": "Nieves Alston",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1406
    },
    {
        "title": "Angie Bates",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8531
    },
    {
        "title": "Bianca Hopper",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2452
    },
    {
        "title": "Violet Holmes",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9469
    },
    {
        "title": "Young Blevins",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5222
    },
    {
        "title": "Whitney Mcintosh",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6563
    },
    {
        "title": "Tricia Quinn",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 632
    },
    {
        "title": "Roslyn Dodson",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4449
    },
    {
        "title": "Harriett Roberts",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7275
    },
    {
        "title": "Claudia Donaldson",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5956
    },
    {
        "title": "Cantu Burnett",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8740
    },
    {
        "title": "Kelly Barber",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5933
    },
    {
        "title": "Peters Burt",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9520
    },
    {
        "title": "Pearson Bird",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4229
    },
    {
        "title": "Wilson Neal",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1633
    },
    {
        "title": "Simon Key",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3123
    },
    {
        "title": "Latisha Carey",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6858
    },
    {
        "title": "Ware Howard",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9134
    },
    {
        "title": "Dawn Moody",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 274
    },
    {
        "title": "Maxine Ashley",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7446
    },
    {
        "title": "Hickman Rich",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7291
    },
    {
        "title": "Jo Carney",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2361
    },
    {
        "title": "Sofia Bond",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8400
    },
    {
        "title": "Maura Franco",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8545
    },
    {
        "title": "Maldonado Shaffer",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8118
    },
    {
        "title": "Pauline Grimes",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6148
    },
    {
        "title": "Dean Moses",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8076
    },
    {
        "title": "Ethel Harper",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5989
    },
    {
        "title": "Moon Nielsen",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5119
    },
    {
        "title": "Mabel Crane",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5257
    },
    {
        "title": "Burgess Hobbs",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6485
    },
    {
        "title": "Chase Macias",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2913
    },
    {
        "title": "Amber Whitley",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6025
    },
    {
        "title": "Tessa Goodwin",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5093
    },
    {
        "title": "Ashlee Anthony",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 859
    },
    {
        "title": "Janell Parks",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2462
    },
    {
        "title": "Rena Reyes",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7207
    },
    {
        "title": "Maxwell Roth",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 385
    },
    {
        "title": "Mccormick Harrison",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7484
    },
    {
        "title": "Underwood Morse",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5238
    },
    {
        "title": "Santos Boyle",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9896
    },
    {
        "title": "Lou Flynn",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1853
    },
    {
        "title": "Fitzpatrick Erickson",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9417
    },
    {
        "title": "Kitty Compton",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7752
    },
    {
        "title": "Velazquez Finley",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5985
    },
    {
        "title": "Black Mason",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3221
    },
    {
        "title": "Greta Michael",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2021
    },
    {
        "title": "Enid Mays",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3351
    },
    {
        "title": "Lenora Eaton",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3538
    },
    {
        "title": "Knapp Caldwell",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6172
    },
    {
        "title": "Park Craig",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7026
    },
    {
        "title": "Valencia Rivers",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8802
    },
    {
        "title": "Barbra Davidson",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2934
    },
    {
        "title": "Clayton Hensley",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7985
    },
    {
        "title": "Rosemarie Downs",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3038
    },
    {
        "title": "Rush Gonzales",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 0
    },
    {
        "title": "Ivy Knox",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8943
    },
    {
        "title": "Carpenter Long",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1065
    },
    {
        "title": "Brittany Zamora",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3670
    },
    {
        "title": "Lee Jensen",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7831
    },
    {
        "title": "Sonya Sloan",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4070
    },
    {
        "title": "Dixon Romero",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1565
    },
    {
        "title": "Welch Small",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7153
    },
    {
        "title": "Meagan Chaney",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6169
    },
    {
        "title": "Juliana Mosley",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8522
    },
    {
        "title": "Donovan Clarke",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2934
    },
    {
        "title": "Ruthie House",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9486
    },
    {
        "title": "Roberta Meyers",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9717
    },
    {
        "title": "Aileen Lindsay",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5100
    },
    {
        "title": "Tabatha Heath",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8359
    },
    {
        "title": "Janine Mullins",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9136
    },
    {
        "title": "Shaw Hunt",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8279
    },
    {
        "title": "Penelope Carter",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 635
    },
    {
        "title": "Koch Rowland",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4150
    },
    {
        "title": "Sharlene Phillips",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8880
    },
    {
        "title": "Adkins Trujillo",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4003
    },
    {
        "title": "Marcy Stuart",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6080
    },
    {
        "title": "Whitley Schroeder",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8203
    },
    {
        "title": "Nichols Wolf",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6267
    },
    {
        "title": "Zimmerman Rosario",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2939
    },
    {
        "title": "Spears Moss",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2437
    },
    {
        "title": "Zamora Schneider",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3908
    },
    {
        "title": "Peggy Wade",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1709
    },
    {
        "title": "Mckenzie Norman",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 593
    },
    {
        "title": "Arnold Sears",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2321
    },
    {
        "title": "Ferguson Mccormick",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7452
    },
    {
        "title": "Preston Page",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9499
    },
    {
        "title": "Jeannine Suarez",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8733
    },
    {
        "title": "Cox Blanchard",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3638
    },
    {
        "title": "Cathryn Mayer",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4758
    },
    {
        "title": "Susana Castro",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4438
    },
    {
        "title": "Moss Alford",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7967
    },
    {
        "title": "Owen Johnson",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4941
    },
    {
        "title": "Tammy Fernandez",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9536
    },
    {
        "title": "Morgan Castaneda",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5165
    },
    {
        "title": "Lynn Cunningham",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6468
    },
    {
        "title": "Horton Whitehead",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2202
    },
    {
        "title": "Sherman Berry",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4343
    },
    {
        "title": "Levy Ware",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5425
    },
    {
        "title": "Sherri Garner",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4917
    },
    {
        "title": "Juliette Stewart",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5057
    },
    {
        "title": "Hopkins Snider",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8970
    },
    {
        "title": "Marcella Miranda",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3605
    },
    {
        "title": "Mcfarland Webster",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5566
    },
    {
        "title": "Tania Gould",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3716
    },
    {
        "title": "Key Klein",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6425
    },
    {
        "title": "Blackburn Serrano",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9147
    },
    {
        "title": "Monroe Sherman",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1015
    },
    {
        "title": "Burns Petersen",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4337
    },
    {
        "title": "Stacy Head",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5624
    },
    {
        "title": "Mcintosh Ayers",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4221
    },
    {
        "title": "Battle Lyons",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5671
    },
    {
        "title": "Griffith Mcbride",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5228
    },
    {
        "title": "Buckner Talley",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1746
    },
    {
        "title": "Rosario Burke",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2655
    },
    {
        "title": "Bowers Mayo",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9953
    },
    {
        "title": "Hallie Copeland",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7453
    },
    {
        "title": "Gabriela Saunders",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9641
    },
    {
        "title": "Jacquelyn Riggs",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6522
    },
    {
        "title": "Jenkins Browning",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 158
    },
    {
        "title": "Romero Marshall",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8572
    },
    {
        "title": "Joann Parker",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3438
    },
    {
        "title": "Brady Frederick",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7293
    },
    {
        "title": "Bryan Burks",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2357
    },
    {
        "title": "Morgan Santana",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5500
    },
    {
        "title": "Chapman Goodman",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1104
    },
    {
        "title": "Mercedes Morris",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7130
    },
    {
        "title": "James Hurley",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6855
    },
    {
        "title": "Shari Sullivan",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2898
    },
    {
        "title": "Henderson Wyatt",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4190
    },
    {
        "title": "Dana Abbott",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7840
    },
    {
        "title": "Thompson Stevenson",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8877
    },
    {
        "title": "Foster Wilcox",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5938
    },
    {
        "title": "Macdonald Lott",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 379
    },
    {
        "title": "Perry Ortega",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4078
    },
    {
        "title": "Jewell Armstrong",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6495
    },
    {
        "title": "Elvia Cabrera",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8127
    },
    {
        "title": "Katie Watson",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6859
    },
    {
        "title": "Aurora Crawford",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9219
    },
    {
        "title": "Eloise Baldwin",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8087
    },
    {
        "title": "Gwendolyn Kinney",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5107
    },
    {
        "title": "Lindsey Burton",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6883
    },
    {
        "title": "Camacho Ryan",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9507
    },
    {
        "title": "Bonner Weber",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4977
    },
    {
        "title": "Malone Campbell",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6238
    },
    {
        "title": "Jackson Simpson",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2605
    },
    {
        "title": "Jillian Johns",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2962
    },
    {
        "title": "Melton Arnold",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7278
    },
    {
        "title": "Carr Riley",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3985
    },
    {
        "title": "Goodwin Baird",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1222
    },
    {
        "title": "Cochran Fox",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1041
    },
    {
        "title": "Ernestine Harmon",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7701
    },
    {
        "title": "Evelyn Harris",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1277
    },
    {
        "title": "Hughes Pope",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3159
    },
    {
        "title": "Shelby Figueroa",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4947
    },
    {
        "title": "Wilder Mathews",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9997
    },
    {
        "title": "Fulton Hahn",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3763
    },
    {
        "title": "Veronica Stone",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9140
    },
    {
        "title": "Stoday Love",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7399
    },
    {
        "title": "Levine Witt",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3793
    },
    {
        "title": "Tran Spears",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6049
    },
    {
        "title": "Hansen Roman",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1431
    },
    {
        "title": "Freida Callahan",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7636
    },
    {
        "title": "Cleveland Massey",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6917
    },
    {
        "title": "Leslie Calderon",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8349
    },
    {
        "title": "Thelma Taylor",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5185
    },
    {
        "title": "Kay Vang",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3733
    },
    {
        "title": "Reba Rosa",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4868
    },
    {
        "title": "Hamilton White",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 638
    },
    {
        "title": "Coleman Gay",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 646
    },
    {
        "title": "Vance Ratliff",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4484
    },
    {
        "title": "Ellis Cannon",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 247
    },
    {
        "title": "Rice Charles",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5204
    },
    {
        "title": "Jacqueline Greer",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8114
    },
    {
        "title": "Rios Sanchez",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 218
    },
    {
        "title": "Stewart Harrington",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3218
    },
    {
        "title": "Velasquez Collins",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3799
    },
    {
        "title": "Theresa Deleon",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5756
    },
    {
        "title": "Bertie Schwartz",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5496
    },
    {
        "title": "Estrada Mcpherson",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 528
    },
    {
        "title": "Murray Bentley",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1163
    },
    {
        "title": "Patrick Powers",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5409
    },
    {
        "title": "Brooke Franklin",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4784
    },
    {
        "title": "Wilda Dunlap",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5382
    },
    {
        "title": "Turner Barnett",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 218
    },
    {
        "title": "Bauer Dominguez",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1838
    },
    {
        "title": "Ellison Molina",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8540
    },
    {
        "title": "Eileen George",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4441
    },
    {
        "title": "Dale Chang",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4818
    },
    {
        "title": "Corinne Lawson",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5967
    },
    {
        "title": "Sandy Wiggins",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 925
    },
    {
        "title": "Rhonda Skinner",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2202
    },
    {
        "title": "Leann Lewis",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9948
    },
    {
        "title": "Rich Preston",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5042
    },
    {
        "title": "Fuentes Wiley",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5336
    },
    {
        "title": "Talley Lucas",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4084
    },
    {
        "title": "Hebert Adkins",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1304
    },
    {
        "title": "Maritza Pacheco",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7191
    },
    {
        "title": "Trisha Murray",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9766
    },
    {
        "title": "Elizabeth Mcfarland",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4871
    },
    {
        "title": "Weeks Pate",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8131
    },
    {
        "title": "Viola Delacruz",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7766
    },
    {
        "title": "Jody Randolph",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4282
    },
    {
        "title": "Savage Mccray",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7216
    },
    {
        "title": "Lorena Hendricks",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7501
    },
    {
        "title": "Franklin Mack",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3083
    },
    {
        "title": "Warren Austin",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2132
    },
    {
        "title": "Hayes Murphy",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1938
    },
    {
        "title": "Bette Mendoza",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6329
    },
    {
        "title": "Mariana Kemp",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8730
    },
    {
        "title": "Christian Sykes",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2130
    },
    {
        "title": "Morin Oneal",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1854
    },
    {
        "title": "Sykes Hall",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4001
    },
    {
        "title": "Allison Pace",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1883
    },
    {
        "title": "Ester Beck",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7896
    },
    {
        "title": "Drake Parrish",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9608
    },
    {
        "title": "Kline Horn",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 480
    },
    {
        "title": "Holt Rosales",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6314
    },
    {
        "title": "Giles Lara",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3367
    },
    {
        "title": "Pope Bush",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6418
    },
    {
        "title": "Boone Jarvis",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6460
    },
    {
        "title": "Valenzuela Cline",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1595
    },
    {
        "title": "Ryan Chan",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8286
    },
    {
        "title": "Pate Fields",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 947
    },
    {
        "title": "Fields Ewing",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1726
    },
    {
        "title": "Rivers Lawrence",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1753
    },
    {
        "title": "Luella Perkins",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8879
    },
    {
        "title": "Diann Hansen",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5251
    },
    {
        "title": "Acosta Holcomb",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3192
    },
    {
        "title": "Lucile Smith",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6055
    },
    {
        "title": "Susan Aguirre",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5937
    },
    {
        "title": "Molina Mcgee",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6203
    },
    {
        "title": "Montoya Burris",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7811
    },
    {
        "title": "Herminia Mcdaniel",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3324
    },
    {
        "title": "Boyd Dixon",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8400
    },
    {
        "title": "Kristen Ortiz",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5496
    },
    {
        "title": "Singleton Mcneil",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7342
    },
    {
        "title": "Alexander Ward",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 458
    },
    {
        "title": "Leah Farrell",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6439
    },
    {
        "title": "Gena Church",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6798
    },
    {
        "title": "Ila Irwin",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3187
    },
    {
        "title": "Hester Mckinney",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1948
    },
    {
        "title": "Tamra Hubbard",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7157
    },
    {
        "title": "Louise Reynolds",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9239
    },
    {
        "title": "Jimmie Richard",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8964
    },
    {
        "title": "Chrystal Tillman",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9946
    },
    {
        "title": "Valeria Vasquez",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4648
    },
    {
        "title": "Mcdowell Le",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 280
    },
    {
        "title": "Essie Boyer",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5174
    },
    {
        "title": "Constance Tyler",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 940
    },
    {
        "title": "Howell Garrison",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 77
    },
    {
        "title": "Bonnie Turner",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7589
    },
    {
        "title": "Sparks Young",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3198
    },
    {
        "title": "Richardson Vinson",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3799
    },
    {
        "title": "Hanson Waters",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5275
    },
    {
        "title": "Deann Allison",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6038
    },
    {
        "title": "Church James",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5740
    },
    {
        "title": "Fletcher Cherry",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7800
    },
    {
        "title": "Solomon Acevedo",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8658
    },
    {
        "title": "Quinn Terry",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6527
    },
    {
        "title": "Armstrong Odonnell",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1201
    },
    {
        "title": "Waller Garrett",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 980
    },
    {
        "title": "Tamara Bernard",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3434
    },
    {
        "title": "Kristina Blake",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1307
    },
    {
        "title": "Sanders Daniel",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4455
    },
    {
        "title": "Oliver Rodriquez",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2462
    },
    {
        "title": "Erika Thornton",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6467
    },
    {
        "title": "Stark Robinson",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 177
    },
    {
        "title": "Maynard Cruz",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2490
    },
    {
        "title": "Danielle Pearson",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7045
    },
    {
        "title": "Leigh Mcdonald",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7330
    },
    {
        "title": "Althea Todd",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4869
    },
    {
        "title": "Good Buckley",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6724
    },
    {
        "title": "Melody Sexton",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1152
    },
    {
        "title": "Nadine Gutierrez",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2127
    },
    {
        "title": "Clements Fuentes",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4680
    },
    {
        "title": "Lott Yang",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3282
    },
    {
        "title": "Dona Nunez",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3192
    },
    {
        "title": "Johanna Warner",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8554
    },
    {
        "title": "Marion Hewitt",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8564
    },
    {
        "title": "Cunningham Clark",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 366
    },
    {
        "title": "Jeanne Koch",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9786
    },
    {
        "title": "Tina French",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1402
    },
    {
        "title": "Charmaine Chavez",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1356
    },
    {
        "title": "Janet Berger",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7143
    },
    {
        "title": "Delacruz Kelly",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 699
    },
    {
        "title": "Etta Lindsey",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7418
    },
    {
        "title": "Larsen Ray",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9108
    },
    {
        "title": "Eunice Mullen",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7619
    },
    {
        "title": "Dee Perry",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6171
    },
    {
        "title": "Shannon Peck",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5508
    },
    {
        "title": "Wynn Barker",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3997
    },
    {
        "title": "Vargas Haney",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1239
    },
    {
        "title": "Schneider Flores",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 897
    },
    {
        "title": "Kathy Hopkins",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7878
    },
    {
        "title": "Annmarie Jordan",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2083
    },
    {
        "title": "Patel Morton",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7846
    },
    {
        "title": "Kelly Pittman",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8329
    },
    {
        "title": "Tasha Fisher",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 872
    },
    {
        "title": "Dotson Dean",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2682
    },
    {
        "title": "Corine Nash",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4803
    },
    {
        "title": "Carrillo Tanner",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3507
    },
    {
        "title": "Alvarez Potts",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1654
    },
    {
        "title": "Mosley Kent",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8335
    },
    {
        "title": "Lamb Mooney",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4120
    },
    {
        "title": "Sosa Mcdowell",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3659
    },
    {
        "title": "Lora Swanson",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4402
    },
    {
        "title": "Marie Cleveland",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9730
    },
    {
        "title": "Carson Weaver",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1768
    },
    {
        "title": "Ball Lee",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6195
    },
    {
        "title": "Bowen Lopez",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6949
    },
    {
        "title": "Hutchinson Pratt",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6785
    },
    {
        "title": "Paulette Houston",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6238
    },
    {
        "title": "Washington Mercer",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9854
    },
    {
        "title": "Elinor Fuller",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8156
    },
    {
        "title": "Oneill Valentine",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2586
    },
    {
        "title": "Joy Joseph",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1483
    },
    {
        "title": "Phyllis Bartlett",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2161
    },
    {
        "title": "Ashley Faulkner",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2440
    },
    {
        "title": "Prince Pennington",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7392
    },
    {
        "title": "Barrett Oconnor",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 336
    },
    {
        "title": "Lacey Gonzalez",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6232
    },
    {
        "title": "Collins Slater",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3718
    },
    {
        "title": "Aisha Ferrell",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3716
    },
    {
        "title": "Carmella Burch",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2125
    },
    {
        "title": "Loretta Mckay",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 305
    },
    {
        "title": "Campbell Kane",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9165
    },
    {
        "title": "Wendi Alvarado",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5479
    },
    {
        "title": "Rosanna Rasmussen",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4575
    },
    {
        "title": "Lester Burns",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9738
    },
    {
        "title": "Rowena Little",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4320
    },
    {
        "title": "Autumn Wells",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 978
    },
    {
        "title": "Francesca Landry",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5406
    },
    {
        "title": "Flowers Hodge",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5822
    },
    {
        "title": "Kenya Huber",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7492
    },
    {
        "title": "Norton Conley",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4853
    },
    {
        "title": "Bobbie Garza",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6165
    },
    {
        "title": "Rosalie Barr",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1182
    },
    {
        "title": "Pittman Stokes",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9062
    },
    {
        "title": "Janis Robertson",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9647
    },
    {
        "title": "Candy Curry",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8546
    },
    {
        "title": "Kellie Hart",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6125
    },
    {
        "title": "Brennan Graham",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 832
    },
    {
        "title": "Gallegos Owen",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6621
    },
    {
        "title": "Barbara Glover",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6332
    },
    {
        "title": "Compton Kramer",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8802
    },
    {
        "title": "Sharp Zimmerman",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7623
    },
    {
        "title": "Tommie Chandler",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2391
    },
    {
        "title": "Mildred Mitchell",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1184
    },
    {
        "title": "Annette Shields",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 429
    },
    {
        "title": "Heidi Nichols",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3808
    },
    {
        "title": "Haley Stephens",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7257
    },
    {
        "title": "Rebecca Holden",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1198
    },
    {
        "title": "York Spencer",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3495
    },
    {
        "title": "Tanya Cummings",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5374
    },
    {
        "title": "Lucia Malone",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8174
    },
    {
        "title": "Bridges Tyson",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6922
    },
    {
        "title": "Adele Oneil",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8113
    },
    {
        "title": "Raquel Valenzuela",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5420
    },
    {
        "title": "Faith Donovan",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7853
    },
    {
        "title": "Natalie Hull",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4235
    },
    {
        "title": "Marquez Dennis",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1568
    },
    {
        "title": "Frank Leon",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1155
    },
    {
        "title": "Tanner Jones",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8962
    },
    {
        "title": "Mccray Duke",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6232
    },
    {
        "title": "Lawanda Hanson",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8653
    },
    {
        "title": "Celia Raymond",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8994
    },
    {
        "title": "Liz Ramsey",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 595
    },
    {
        "title": "Hoffman Fitzpatrick",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 36
    },
    {
        "title": "Jerri Pugh",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4326
    },
    {
        "title": "Beatriz Holloway",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8050
    },
    {
        "title": "Rodgers Garcia",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7191
    },
    {
        "title": "Nadia Higgins",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 247
    },
    {
        "title": "Maricela Townsend",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1884
    },
    {
        "title": "Gilliam Stanton",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2752
    },
    {
        "title": "Sweeney Cooper",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5320
    },
    {
        "title": "Larson Harvey",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6869
    },
    {
        "title": "Doreen Parsons",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8214
    },
    {
        "title": "Queen Levine",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 49
    },
    {
        "title": "Mavis Lynch",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9682
    },
    {
        "title": "Jean Powell",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1894
    },
    {
        "title": "Barlow Brady",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8748
    },
    {
        "title": "Maggie Williamson",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3632
    },
    {
        "title": "Teri Rivera",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2530
    },
    {
        "title": "Chasity Henderson",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3411
    },
    {
        "title": "Haley Fowler",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6544
    },
    {
        "title": "Christa Marquez",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9317
    },
    {
        "title": "Lena Kirby",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 530
    },
    {
        "title": "Deirdre Morales",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5027
    },
    {
        "title": "Ella Shelton",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1936
    },
    {
        "title": "Janie Robbins",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2220
    },
    {
        "title": "Whitaker Rocha",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9604
    },
    {
        "title": "Gross Estes",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7348
    },
    {
        "title": "Combs Larson",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6245
    },
    {
        "title": "Bates Huffman",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4720
    },
    {
        "title": "Marquita Rodriguez",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3632
    },
    {
        "title": "Tammie Richmond",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1551
    },
    {
        "title": "Rosanne Reilly",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1504
    },
    {
        "title": "Barry Barrera",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6651
    },
    {
        "title": "Hope Barry",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3553
    },
    {
        "title": "Janelle Lowery",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2637
    },
    {
        "title": "Stephenson Terrell",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5232
    },
    {
        "title": "Debbie Velez",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5399
    },
    {
        "title": "Kelli Griffin",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6606
    },
    {
        "title": "Alta Merrill",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6704
    },
    {
        "title": "Daphne Goff",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 329
    },
    {
        "title": "Nunez Whitaker",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2952
    },
    {
        "title": "Marsh Vaughan",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3851
    },
    {
        "title": "Shelia Maynard",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1015
    },
    {
        "title": "Terry Cooley",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1384
    },
    {
        "title": "Margaret Miles",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9024
    },
    {
        "title": "Rasmussen Patton",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2323
    },
    {
        "title": "Riley Gill",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7952
    },
    {
        "title": "Staci Sharpe",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9530
    },
    {
        "title": "Randolph May",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6636
    },
    {
        "title": "Clarice Clayton",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6741
    },
    {
        "title": "Leila Dejesus",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8037
    },
    {
        "title": "Kemp Jefferson",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4927
    },
    {
        "title": "Myrna Avery",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8929
    },
    {
        "title": "Ursula Henson",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2795
    },
    {
        "title": "Sheena Bryant",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8518
    },
    {
        "title": "Brown Wong",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1620
    },
    {
        "title": "Cole Warren",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2191
    },
    {
        "title": "Mcbride Santiago",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 336
    },
    {
        "title": "Keisha William",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5630
    },
    {
        "title": "Hart Bowen",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3564
    },
    {
        "title": "Olsen Meyer",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8335
    },
    {
        "title": "Lisa Curtis",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9843
    },
    {
        "title": "Elise Pickett",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3954
    },
    {
        "title": "Kim Cotton",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3159
    },
    {
        "title": "Guthrie Lester",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1168
    },
    {
        "title": "Moody Horne",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5185
    },
    {
        "title": "Wyatt Jacobs",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9447
    },
    {
        "title": "Chelsea Marks",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7759
    },
    {
        "title": "Hattie Kirkland",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9
    },
    {
        "title": "Lynn Howe",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1253
    },
    {
        "title": "Mindy Osborn",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7928
    },
    {
        "title": "Bettie Walker",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3477
    },
    {
        "title": "Patrice Guzman",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9601
    },
    {
        "title": "Reyes Potter",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6923
    },
    {
        "title": "Clemons Mcleod",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2926
    },
    {
        "title": "Parks Lamb",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5372
    },
    {
        "title": "Tracy Collier",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6128
    },
    {
        "title": "Madge Reed",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2767
    },
    {
        "title": "Daisy Finch",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3654
    },
    {
        "title": "Simpson Becker",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3005
    },
    {
        "title": "Angelique Galloway",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 615
    },
    {
        "title": "Sarah Valencia",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1565
    },
    {
        "title": "England Olsen",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6268
    },
    {
        "title": "Deanne Wood",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7253
    },
    {
        "title": "Kelley Clements",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1795
    },
    {
        "title": "Vera Rutledge",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6820
    },
    {
        "title": "Ladonna Greene",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6946
    },
    {
        "title": "Hunter Floyd",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7038
    },
    {
        "title": "Deana Gaines",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4208
    },
    {
        "title": "Osborn Cash",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5140
    },
    {
        "title": "Oconnor Ellis",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 726
    },
    {
        "title": "Randall Andrews",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2645
    },
    {
        "title": "Butler Hardin",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6492
    },
    {
        "title": "Miranda Sims",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5216
    },
    {
        "title": "Blankenship Mccarty",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2154
    },
    {
        "title": "Eugenia Gardner",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3361
    },
    {
        "title": "Meghan Livingston",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6791
    },
    {
        "title": "Pennington Stanley",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4243
    },
    {
        "title": "Sampson Guerrero",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5713
    },
    {
        "title": "Jewel Duran",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9756
    },
    {
        "title": "Walls Hines",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 151
    },
    {
        "title": "Knox Buckner",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9699
    },
    {
        "title": "Latonya Boone",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 188
    },
    {
        "title": "Emerson Hale",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9325
    },
    {
        "title": "Katy Paul",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4830
    },
    {
        "title": "Wong Myers",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7395
    },
    {
        "title": "Trudy Wilkerson",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6243
    },
    {
        "title": "Laurie Maxwell",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3884
    },
    {
        "title": "Mclean Golden",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1290
    },
    {
        "title": "Rachelle Atkins",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9566
    },
    {
        "title": "Katharine Hurst",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5762
    },
    {
        "title": "Kristy Gray",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5993
    },
    {
        "title": "Ina Christensen",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3458
    },
    {
        "title": "Marva Frazier",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 859
    },
    {
        "title": "Bray Crosby",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8865
    },
    {
        "title": "Natasha Blackburn",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7631
    },
    {
        "title": "Carlene Horton",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8122
    },
    {
        "title": "Alston Wynn",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7005
    },
    {
        "title": "Roxie Sandoval",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2767
    },
    {
        "title": "Anna Haley",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3927
    },
    {
        "title": "Adrian Rios",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9412
    },
    {
        "title": "Hampton Good",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 803
    },
    {
        "title": "Sheppard Meadows",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1746
    },
    {
        "title": "Hooper Holder",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3735
    },
    {
        "title": "Monica Oneill",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2516
    },
    {
        "title": "Barnett Mcintyre",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7991
    },
    {
        "title": "Erin Ramos",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6363
    },
    {
        "title": "Norman Mcclure",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9126
    },
    {
        "title": "Tracie Jacobson",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1931
    },
    {
        "title": "Gill Woodward",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7859
    },
    {
        "title": "Henson Martin",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7330
    },
    {
        "title": "Wheeler Bender",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5905
    },
    {
        "title": "Sheri Giles",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8798
    },
    {
        "title": "Wilkins Gamble",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7368
    },
    {
        "title": "Mari Aguilar",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4990
    },
    {
        "title": "Trevino York",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2437
    },
    {
        "title": "Cecelia England",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7241
    },
    {
        "title": "Christina Bell",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8791
    },
    {
        "title": "Faye Madden",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 386
    },
    {
        "title": "Conner Prince",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9432
    },
    {
        "title": "Melanie Green",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1298
    },
    {
        "title": "Mclaughlin Barnes",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2716
    },
    {
        "title": "Cook Mccullough",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6631
    },
    {
        "title": "Bishop Walton",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6691
    },
    {
        "title": "Lane Dale",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8953
    },
    {
        "title": "Eaton Stevens",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7384
    },
    {
        "title": "Rachael Harding",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7223
    },
    {
        "title": "Sonja Nicholson",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5408
    },
    {
        "title": "Hartman Logan",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8467
    },
    {
        "title": "Lindsay Farmer",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 914
    },
    {
        "title": "Lynda Ford",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9022
    },
    {
        "title": "Lilia Colon",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6786
    },
    {
        "title": "Maryanne Melton",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8465
    },
    {
        "title": "Bender Diaz",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5166
    },
    {
        "title": "Cornelia Duffy",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6345
    },
    {
        "title": "Workman Mueller",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 571
    },
    {
        "title": "Mcmahon Patterson",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1728
    },
    {
        "title": "Taylor Hodges",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8248
    },
    {
        "title": "Sawyer Cole",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4592
    },
    {
        "title": "Chandler Fletcher",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9821
    },
    {
        "title": "Cleo Vincent",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 886
    },
    {
        "title": "Wilma Hayden",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4887
    },
    {
        "title": "Francis Martinez",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1145
    },
    {
        "title": "Cash Valdez",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9479
    },
    {
        "title": "Wooten Foreman",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5154
    },
    {
        "title": "Marina Keith",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6671
    },
    {
        "title": "Effie Hancock",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5805
    },
    {
        "title": "Todd Rollins",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4300
    },
    {
        "title": "Luann Puckett",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2135
    },
    {
        "title": "Stephens Robles",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7043
    },
    {
        "title": "Moore Foley",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 18
    },
    {
        "title": "Claire Holt",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 457
    },
    {
        "title": "Dunlap Buchanan",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 17
    },
    {
        "title": "Helena Mcknight",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5149
    },
    {
        "title": "Fanny Jennings",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8180
    },
    {
        "title": "Ruth Ball",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7813
    },
    {
        "title": "Eva Poole",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3119
    },
    {
        "title": "Abigail Gates",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6563
    },
    {
        "title": "Lottie Pruitt",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3122
    },
    {
        "title": "Dorsey Kerr",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1671
    },
    {
        "title": "Woods Pollard",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8538
    },
    {
        "title": "Frederick Banks",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2436
    },
    {
        "title": "Herring Shannon",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6773
    },
    {
        "title": "Vilma Hogan",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2583
    },
    {
        "title": "Patricia Mclean",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4011
    },
    {
        "title": "Robles Macdonald",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8721
    },
    {
        "title": "Hensley Tran",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3789
    },
    {
        "title": "Wade Fischer",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6341
    },
    {
        "title": "Tamera Wise",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8185
    },
    {
        "title": "Caitlin Wagner",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3756
    },
    {
        "title": "Silva Byrd",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4278
    },
    {
        "title": "Judy Boyd",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2665
    },
    {
        "title": "Acevedo Gentry",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1219
    },
    {
        "title": "Jami Riddle",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 51
    },
    {
        "title": "Helen Hendrix",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8090
    },
    {
        "title": "Bean Noble",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6055
    },
    {
        "title": "Mason Vaughn",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7529
    },
    {
        "title": "Osborne Welch",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7766
    },
    {
        "title": "Shanna Calhoun",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 529
    },
    {
        "title": "Misty Benjamin",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7323
    },
    {
        "title": "Geraldine Salas",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5415
    },
    {
        "title": "Gladys Hardy",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3962
    },
    {
        "title": "Glenn Leonard",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2874
    },
    {
        "title": "Jennings Hoffman",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 330
    },
    {
        "title": "Chang Patel",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6223
    },
    {
        "title": "Luna Nelson",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7519
    },
    {
        "title": "Elnora Shepherd",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2472
    },
    {
        "title": "Jessica West",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8960
    },
    {
        "title": "Espinoza Barron",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4922
    },
    {
        "title": "Vinson Simmons",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7973
    },
    {
        "title": "Austin Weiss",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9438
    },
    {
        "title": "Wright Shaw",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2921
    },
    {
        "title": "Letitia Bonner",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2597
    },
    {
        "title": "Johnson Davis",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2757
    },
    {
        "title": "Beverly Fitzgerald",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5035
    },
    {
        "title": "Ramsey Summers",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6100
    },
    {
        "title": "Summers Waller",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1849
    },
    {
        "title": "Roth Holman",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4156
    },
    {
        "title": "Tanisha Solis",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5547
    },
    {
        "title": "Mae King",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7929
    },
    {
        "title": "Joan Dawson",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5701
    },
    {
        "title": "Barnes Cardenas",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1084
    },
    {
        "title": "Katrina Melendez",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 259
    },
    {
        "title": "Landry Cantu",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6957
    },
    {
        "title": "Erma Kirk",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6188
    },
    {
        "title": "Lesley Lloyd",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1427
    },
    {
        "title": "Elsa Bradford",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2269
    },
    {
        "title": "Penny Bright",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1087
    },
    {
        "title": "Vincent Gallegos",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5978
    },
    {
        "title": "Ana Adams",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6380
    },
    {
        "title": "Dena Sparks",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2419
    },
    {
        "title": "Moses Benton",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4357
    },
    {
        "title": "Leanne Mckenzie",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2758
    },
    {
        "title": "Patsy Durham",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5444
    },
    {
        "title": "Kaye Mejia",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1547
    },
    {
        "title": "Benson Hicks",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7294
    },
    {
        "title": "Jensen Walls",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2854
    },
    {
        "title": "Gwen Savage",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9552
    },
    {
        "title": "Rosetta Rush",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4823
    },
    {
        "title": "Rochelle Vazquez",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3017
    },
    {
        "title": "Socorro Mccarthy",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6624
    },
    {
        "title": "Delaney Whitney",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3713
    },
    {
        "title": "Gallagher Newton",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5972
    },
    {
        "title": "Debora Battle",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1579
    },
    {
        "title": "Stokes Lang",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7453
    },
    {
        "title": "Little Palmer",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7957
    },
    {
        "title": "Kayla Dalton",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 670
    },
    {
        "title": "Stephanie Wall",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5436
    },
    {
        "title": "Lois Branch",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9797
    },
    {
        "title": "Hunt Villarreal",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3724
    },
    {
        "title": "Lana Shepard",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2041
    },
    {
        "title": "Avila Byers",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4399
    },
    {
        "title": "Roy Gilmore",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 757
    },
    {
        "title": "Fox Luna",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9658
    },
    {
        "title": "Deena Peters",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6154
    },
    {
        "title": "Dorthy Spence",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8384
    },
    {
        "title": "Winnie Roach",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 64
    },
    {
        "title": "Robyn Price",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 900
    },
    {
        "title": "Shannon Simon",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4540
    },
    {
        "title": "Elva Thompson",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 849
    },
    {
        "title": "Weaver Kaufman",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4760
    },
    {
        "title": "Gonzalez Bryan",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2773
    },
    {
        "title": "Traci Wilkins",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9586
    },
    {
        "title": "Willie Bray",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8530
    },
    {
        "title": "Castro Vance",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7027
    },
    {
        "title": "Dale Bullock",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2962
    },
    {
        "title": "Silvia Alvarez",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8816
    },
    {
        "title": "Tammi Frost",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4111
    },
    {
        "title": "Katelyn Pierce",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6611
    },
    {
        "title": "Gale Wilson",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6191
    },
    {
        "title": "Bond Gross",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2803
    },
    {
        "title": "Betsy Walter",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7144
    },
    {
        "title": "Verna Moore",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7866
    },
    {
        "title": "Branch Baker",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9192
    },
    {
        "title": "Ewing Langley",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5177
    },
    {
        "title": "Ericka Oliver",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1726
    },
    {
        "title": "Shepard Tate",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6286
    },
    {
        "title": "Lorene Yates",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 364
    },
    {
        "title": "Mcclure Hatfield",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5944
    },
    {
        "title": "Michael Mckee",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6250
    },
    {
        "title": "Ophelia Camacho",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3698
    },
    {
        "title": "Charity Booker",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4816
    },
    {
        "title": "Terri Blankenship",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2288
    },
    {
        "title": "Harriet Francis",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9609
    },
    {
        "title": "Gaines Nolan",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6760
    },
    {
        "title": "Megan Morrow",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 464
    },
    {
        "title": "Patty Christian",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2218
    },
    {
        "title": "Aida Herrera",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 500
    },
    {
        "title": "Bright Sheppard",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 93
    },
    {
        "title": "Callie Anderson",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2762
    },
    {
        "title": "Buchanan Conrad",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3406
    },
    {
        "title": "Jones Beard",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7616
    },
    {
        "title": "Mable Cooke",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7867
    },
    {
        "title": "Hancock Graves",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5511
    },
    {
        "title": "Lee Reeves",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1097
    },
    {
        "title": "Lorrie Forbes",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6027
    },
    {
        "title": "Cline Dillard",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5393
    },
    {
        "title": "Hillary Ayala",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3686
    },
    {
        "title": "Imogene Richardson",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2316
    },
    {
        "title": "Adeline Watkins",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6018
    },
    {
        "title": "Brenda Dorsey",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4573
    },
    {
        "title": "Sherry Hayes",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6928
    },
    {
        "title": "Lea Levy",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6049
    },
    {
        "title": "Ingram Owens",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4020
    },
    {
        "title": "Holly Morrison",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8436
    },
    {
        "title": "Elma Patrick",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7422
    },
    {
        "title": "Alfreda Bradley",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3995
    },
    {
        "title": "Rosales Henry",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 678
    },
    {
        "title": "Freeman Beasley",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4256
    },
    {
        "title": "Walsh Hughes",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9789
    },
    {
        "title": "Joanne Hooper",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3435
    },
    {
        "title": "Lorraine Howell",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8204
    },
    {
        "title": "Fisher Freeman",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3158
    },
    {
        "title": "Madden Bolton",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2963
    },
    {
        "title": "Fannie Jenkins",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3149
    },
    {
        "title": "Page Juarez",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1991
    },
    {
        "title": "Kristie Coleman",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8698
    },
    {
        "title": "Nolan Roy",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9855
    },
    {
        "title": "Blanca Mann",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4321
    },
    {
        "title": "Melisa Brooks",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6246
    },
    {
        "title": "Julia Craft",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4339
    },
    {
        "title": "Beard Vargas",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3444
    },
    {
        "title": "Pansy Brewer",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2296
    },
    {
        "title": "Finley Moreno",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 448
    },
    {
        "title": "Riddle Allen",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 509
    },
    {
        "title": "Rosalind Davenport",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7782
    },
    {
        "title": "Bird Mcgowan",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 37
    },
    {
        "title": "Knight Guerra",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4248
    },
    {
        "title": "Celeste Thomas",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 338
    },
    {
        "title": "Herman Mclaughlin",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1213
    },
    {
        "title": "Krista Clay",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7905
    },
    {
        "title": "Wilkerson Conner",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8187
    },
    {
        "title": "Margret Gibbs",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3819
    },
    {
        "title": "Minnie Phelps",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5512
    },
    {
        "title": "Mann Evans",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7656
    },
    {
        "title": "Ford Pena",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2098
    },
    {
        "title": "Cindy Delaney",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7563
    },
    {
        "title": "Lowe Daugherty",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7051
    },
    {
        "title": "Maria Padilla",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7613
    },
    {
        "title": "Morse Kidd",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5485
    },
    {
        "title": "Hess Tucker",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5059
    },
    {
        "title": "Melba Barton",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1538
    },
    {
        "title": "Adrienne Kline",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7419
    },
    {
        "title": "Payne Douglas",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4817
    },
    {
        "title": "Ilene Clemons",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2562
    },
    {
        "title": "Foreman Stark",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7531
    },
    {
        "title": "Olson Guy",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7398
    },
    {
        "title": "Nola Black",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2303
    },
    {
        "title": "Keller Brown",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2955
    },
    {
        "title": "Robert Joyce",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 876
    },
    {
        "title": "Tonia Hamilton",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4951
    },
    {
        "title": "Rocha Bishop",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4734
    },
    {
        "title": "Carlson Sweeney",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7475
    },
    {
        "title": "Winifred Montgomery",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8299
    },
    {
        "title": "Stacey Conway",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1251
    },
    {
        "title": "Taylor Foster",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3254
    },
    {
        "title": "Suzette Sosa",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6977
    },
    {
        "title": "Ashley Schultz",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6112
    },
    {
        "title": "Soto Chase",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3843
    },
    {
        "title": "Haynes Flowers",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7505
    },
    {
        "title": "Ochoa Medina",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1175
    },
    {
        "title": "Slater Keller",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8185
    },
    {
        "title": "Dionne Alexander",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9856
    },
    {
        "title": "Noreen Rojas",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4521
    },
    {
        "title": "Green Strickland",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4492
    },
    {
        "title": "Callahan Velasquez",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2966
    },
    {
        "title": "Sadie Lowe",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 475
    },
    {
        "title": "Mayer Everett",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3939
    },
    {
        "title": "Reva Franks",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2591
    },
    {
        "title": "Scott Wallace",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6073
    },
    {
        "title": "Gibson Stout",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1959
    },
    {
        "title": "Nellie Hartman",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4595
    },
    {
        "title": "Mcdaniel Ochoa",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8619
    },
    {
        "title": "Glenna Rodgers",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9557
    },
    {
        "title": "Padilla Sweet",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4217
    },
    {
        "title": "Lucas Hawkins",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1489
    },
    {
        "title": "Beck Munoz",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1387
    },
    {
        "title": "Smith Burgess",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4568
    },
    {
        "title": "Mitchell Ingram",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3910
    },
    {
        "title": "Ferrell Delgado",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2553
    },
    {
        "title": "Paula Knight",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4742
    },
    {
        "title": "Frankie Casey",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5584
    },
    {
        "title": "Gray Ruiz",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3964
    },
    {
        "title": "Leon Newman",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9721
    },
    {
        "title": "Sullivan Bailey",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 306
    },
    {
        "title": "Carolyn Noel",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9377
    },
    {
        "title": "Day Farley",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3637
    },
    {
        "title": "Alicia Travis",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8731
    },
    {
        "title": "Jessie Carroll",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1654
    },
    {
        "title": "Hewitt Hyde",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9725
    },
    {
        "title": "Erica Bass",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 873
    },
    {
        "title": "Dianne English",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2857
    },
    {
        "title": "Frieda Dudley",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4147
    },
    {
        "title": "Connie Norris",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2935
    },
    {
        "title": "Edna Sampson",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2213
    },
    {
        "title": "Brigitte Glass",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7589
    },
    {
        "title": "Chan Bennett",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8156
    },
    {
        "title": "Pearl Fleming",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6366
    },
    {
        "title": "Bruce Cortez",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7039
    },
    {
        "title": "Lynette Chambers",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3143
    },
    {
        "title": "Anthony Carver",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7904
    },
    {
        "title": "Shawn Blackwell",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1669
    },
    {
        "title": "Guy Acosta",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1252
    },
    {
        "title": "Jordan Buck",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2839
    },
    {
        "title": "Pugh Bradshaw",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1528
    },
    {
        "title": "Atkinson Mcconnell",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 6245
    },
    {
        "title": "Gates Mcfadden",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5907
    },
    {
        "title": "Parker Maldonado",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4400
    },
    {
        "title": "Merle Hester",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6064
    },
    {
        "title": "Stuart Vega",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7826
    },
    {
        "title": "Kate Grant",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5551
    },
    {
        "title": "Jannie Hinton",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9397
    },
    {
        "title": "Earnestine Wolfe",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7469
    },
    {
        "title": "Ayers Cantrell",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3636
    },
    {
        "title": "Ada Odom",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9357
    },
    {
        "title": "Martina Cox",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4606
    },
    {
        "title": "Oneil Orr",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2829
    },
    {
        "title": "Witt Torres",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7962
    },
    {
        "title": "Salinas Ramirez",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5407
    },
    {
        "title": "Thomas Solomon",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 85
    },
    {
        "title": "Kelley Sawyer",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8478
    },
    {
        "title": "Amanda Rogers",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3138
    },
    {
        "title": "Kent Lynn",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2566
    },
    {
        "title": "Clarke Berg",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7844
    },
    {
        "title": "Reese Osborne",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8832
    },
    {
        "title": "Liliana Randall",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1989
    },
    {
        "title": "Cantrell Mcmahon",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1791
    },
    {
        "title": "Schwartz Joyner",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4722
    },
    {
        "title": "Jeanette Kelley",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7394
    },
    {
        "title": "Ayala Rhodes",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1315
    },
    {
        "title": "Mcpherson Frye",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4055
    },
    {
        "title": "Dixie Cameron",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8985
    },
    {
        "title": "Mcconnell Bruce",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5166
    },
    {
        "title": "Freda Best",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4238
    },
    {
        "title": "Ava Hickman",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6774
    },
    {
        "title": "Shields Briggs",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 9900
    },
    {
        "title": "Greene Washington",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1758
    },
    {
        "title": "Ramirez Montoya",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2538
    },
    {
        "title": "Cohen Scott",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2189
    },
    {
        "title": "Lilian Sellers",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7089
    },
    {
        "title": "Esperanza Hess",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3148
    },
    {
        "title": "Pamela Stephenson",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2512
    },
    {
        "title": "Natalia Dunn",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6281
    },
    {
        "title": "Hester Huff",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2248
    },
    {
        "title": "Mendoza Stafford",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4337
    },
    {
        "title": "Magdalena Mathis",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4888
    },
    {
        "title": "Parsons Dyer",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8910
    },
    {
        "title": "Klein Lane",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5329
    },
    {
        "title": "Villarreal Humphrey",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 7894
    },
    {
        "title": "Anderson Dillon",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3251
    },
    {
        "title": "Kennedy Brennan",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5001
    },
    {
        "title": "Maryellen Haynes",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4948
    },
    {
        "title": "Nettie Harrell",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5382
    },
    {
        "title": "Velma Blair",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 7422
    },
    {
        "title": "Miranda Castillo",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 1293
    },
    {
        "title": "Craft Singleton",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4576
    },
    {
        "title": "Shauna Nieves",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4408
    },
    {
        "title": "Deloris Herring",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 603
    },
    {
        "title": "Vaughn Hill",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1214
    },
    {
        "title": "Alisha Decker",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5104
    },
    {
        "title": "Forbes Hebert",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3598
    },
    {
        "title": "Harrington Willis",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3628
    },
    {
        "title": "Jenny Leach",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8352
    },
    {
        "title": "Evangelina Gregory",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8208
    },
    {
        "title": "Leach Matthews",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1298
    },
    {
        "title": "Downs Strong",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 514
    },
    {
        "title": "Antonia Reese",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 8500
    },
    {
        "title": "Graves Campos",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 4694
    },
    {
        "title": "Mcleod Ross",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 5332
    },
    {
        "title": "Briggs Albert",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 3025
    },
    {
        "title": "Marisol Bauer",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 2628
    },
    {
        "title": "Rodriquez Fulton",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 8928
    },
    {
        "title": "Gregory Carrillo",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 1662
    },
    {
        "title": "Marta Contreras",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 6750
    },
    {
        "title": "Russell Monroe",
        "authors": [authors[0]],
        "publish_date": datetime.datetime.today(),
        "type": "Fiction",
        "copies": 2354
    },
    {
        "title": "Lidia Case",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5326
    },
    {
        "title": "Iva Estrada",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 4006
    },
    {
        "title": "Corina Walters",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 9603
    },
    {
        "title": "Melissa Park",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 3620
    },
    {
        "title": "Candice Steele",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 337
    },
    {
        "title": "Jaime Olson",
        "authors": [authors[1]],
        "publish_date": datetime.datetime.today(),
        "type": "Non-Fiction",
        "copies": 5268
    }
]
    
    book_collection = production.book
    book_collection.insert_many(books)

def search_using_regex():
    books_contains_a = production.book.find({"title":{"$regex":"^A"}})
    printer.pprint(list(books_contains_a))

def join_operation():
    author_n_books = production.author.aggregate([{
        "$lookup":{
            "from": "book",
            "localField":"_id",
            "foreignField": "authors",
            "as": "book"
        }
    }])
    printer.pprint(list(author_n_books))
    
def aggregation_pipelane():
    count_books = production.author.aggregate([
    {
        "$lookup":{
            "from": "book",
            "localField":"_id",
            "foreignField": "authors",
            "as": "books"
        }
    },
    {
        "$addFields": {
            "total_books":{"$size":"$books"}
        }
    },
    {
        "$project": {
            "first_name":1, "last_name":1, "total_books":1, "_id": 0
        }
    }
    ])
    printer.pprint(list(count_books))

def aggregation_pipelane_with_map():
    books_with_random_age_authors = production.book.aggregate([
        {
            "$lookup":{
                "from":"author",
                "localField":"authors",
                "foreignField":"_id",
                "as":"authors"
            }
        },
        {
            "$set":{
                "authors":{
                    "$map":{
                        "input":"$authors",
                        "in":{
                            "age":{
                                "$dateDiff":{
                                    "startDate": "$$this.date_of_birth",
                                    "endDate": "$$NOW",
                                    "unit":"year"
                                }
                            },
                            "first_name": "$$this.first_name",
                            "last_name": "$$this.last_name"
                        }
                    }
                }
            }
        },
        {
            "$match":{
                "$and":[
                    {"authors.age":{"$gte":0}},
                    {"authors.age":{"$lte":100}}
                ]
            }
        },
        {
            "$sort":{
                "authors.age": 1 # 1 = asc, 0 = desc
            }
        }
    ])
    printer.pprint(list(books_with_random_age_authors))

