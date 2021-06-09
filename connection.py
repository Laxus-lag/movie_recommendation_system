
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
df = db.new_db.aggregate([
    {"$project": {
        "_id": False,
        "Title": True,
        "Year": True,
        "Short Summary": True,
        "Genres": 
		{
			"$replaceAll": 
			{
				"input": "$Genres", "find": "|", "replacement": " "
			}
		},
        "YouTube Trailer": True,
        "Rating": True,
        "Director": True,
        "Writers": True,
        "Cast": True,
        "Index": True
    }
    }
])
data = list(df)

#############################


##############################