from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://laxus:8057@cluster0.kzdxa.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database('Database')

###############################
db.new_db.update_many(
   { "Writers": "__" },
   { "$set":
      {
        "Writers": " "
      }
   }
)

################################
