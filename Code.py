import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import difflib

##	Step 1: Read CSV File	##

movie_df = pd.read_csv("dataset.csv")

##	Step 2: Cleaning Dataset##

movie_df['Cast'] = movie_df['Cast'].str.replace('|',' ',regex=True)
movie_df['Writers'] =movie_df['Writers'].str.replace('|',' ',regex=True)
items = ['Title','Genres','Director','Cast','Writers']

for feature in items:
	movie_df[feature] = movie_df[feature].fillna("")

##	Step 3: Required selected features are combined	##

def combine_items(row):
	try:
		return (row['Title'] 
		+" "
		+row["Genres"] 
		+" "
		+row["Director"]
		+ " "
		+ row["Cast"]
		+ " "
		+ row["Writers"])
	except():
		print ("Error in Search:", row)

#	Function for taking the user liked movie input and
#   finding similar movies	to return to user which user will like by
#   using count matrix and cosine similarity base on count matrix
#commit

def func(input_movies):
	
	year = []
	poster = []
	movies = []
	genre = []
	rating = []
	summary = []
	
	movie_df["feature"] = movie_df.apply(combine_items,axis=1)
	
	movies_title_list = movie_df['Title'].tolist()
	common_title = difflib.get_close_matches(input_movies, movies_title_list, 1)
	if len(common_title) ==0:
		return movies, poster, year, genre, rating, summary
	title_sim = common_title[0]
	movie_index_from_database = movie_df[movie_df.Title == title_sim]["Index"].values[0]
	
	cv = CountVectorizer()

	count_matrix = cv.fit_transform(movie_df["feature"])
	cosine_sim = cosine_similarity(count_matrix) 

	similar_movie_list =  list(enumerate(cosine_sim[movie_index_from_database]))
	similar_sort_movies = sorted(similar_movie_list,key=lambda x:x[1],reverse=True)
	
	i=0

	for element in similar_sort_movies:
			if i>10:
				break	
			movies.append(movie_df[movie_df.Index == element[0]]["Title"].values[0])
			poster.append(movie_df[movie_df.Index == element[0]]["YouTube Trailer"].values[0])
			year.append(movie_df[movie_df.Index == element[0]]["Year"].values[0])
			genre.append(movie_df[movie_df.Index == element[0]]["Genres"].values[0])
			rating.append(movie_df[movie_df.Index == element[0]]["Rating"].values[0])
			summary.append(movie_df[movie_df.Index == element[0]]["Short Summary"].values[0])
			i+=1
			
	return movies,poster,year,genre,rating,summary
