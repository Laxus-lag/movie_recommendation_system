from pymongo import MongoClient
client = MongoClient(
    "mongodb+srv://laxus:8057@cluster0.kzdxa.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database('Movie_Database')

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
def initial():
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
        "Cast": {
                "$replaceAll":
        {
                        "input": "$Cast", "find": "|", "replacement": " "
        }
        },
        "Index": True
    }
    }
    ])
    return df 
data = list(initial())

#############################
i=0
def data_insert(name, genre, cast, director, writer, summary, poster,year,rating):
    name=str(name)
    genre=str(genre)
    cast=str(cast)
    director=str(director)
    writer=str(writer)
    summary=str(summary)
    poster=str(poster)
    year=str(year)
    rating=str(rating)
    index=str(len(data))
    for item in data:
        if item['Title'] ==name:
            return 1
    print(type(index))
    mydata = {"Title":name, "Year":year, "Short Summary":summary, "Genres":genre, "YouTube Trailer":poster,"Rating":rating,"Director":director,"Writers":writer,"Cast":cast,"Index":index}
    db.new_db.insert_one(mydata)
    data.append(mydata)
    print(len(data))
    return 0
    
##############################
