import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from difflib import get_close_matches
from connection import db
from connection import data

#############################################
##	Step 1: Read CSV File	##
title =[]
feature =[]
#movie_df = pd.read_csv("dataset.csv")

#############################################
##	Step 2: Cleaning Dataset##

for item in data:
    title.append(item['Title'])
    feature.append(item['Title'] 
	+ " "
	+item['Genres'] 
	+ " "
	+item['Director'] 
	+ " " 
	+ item['Writers'] 
	+ " " 
	+ item['Cast'])

# movie_df['Cast'] = movie_df['Cast'].str.replace('|',' ',regex=True)
# movie_df['Writers'] =movie_df['Writers'].str.replace('|',' ',regex=True)
# items = ['Title','Genres','Director','Cast','Writers']

# for feature in items:
# 	movie_df[feature] = movie_df[feature].fillna(" ")
# movie_df.to_csv(r'D:\file3.csv', index=False)

#############################################

##	Step 3: Required selected features are combined	##

# def combine_items(row):
# 	try:
# 		return (row['Title'] 
# 		+" "
# 		+row["Genres"] 
# 		+" "
# 		+row["Director"]
# 		+ " "
# 		+ row["Cast"]
# 		+ " "
# 		+ row["Writers"])
# 	except():
# 		print ("Error in Search:", row)

#############################################

#	Function for taking the user liked movie input and
#   finding similar movies	to return to user which user will like by
#   using count matrix and cosine similarity base on count matrix

def func(input_movies):
	
	year = []
	poster = []
	movies = []
	genre = []
	rating = []
	summary = []
	common_title =get_close_matches(input_movies,title,1)
	# movie_df["feature"] = movie_df.apply(combine_items,axis=1)
	
	# movies_title_list = movie_df['Title'].tolist()
	# common_title = difflib.get_close_matches(input_movies, movies_title_list, 1)
	if len(common_title) ==0:
		return movies, poster, year, genre, rating, summary
	title_sim = common_title[0]
	movie_index_from_database = title.index(title_sim)
	# movie_index_from_database = movie_df[movie_df.Title == title_sim]["Index"].values[0]
	
	cv = CountVectorizer()

	count_matrix = cv.fit_transform(feature)
	cosine_sim = cosine_similarity(count_matrix) 

	similar_movie_list =  list(enumerate(cosine_sim[movie_index_from_database]))
	similar_sort_movies = sorted(similar_movie_list,key=lambda x:x[1],reverse=True)
	
	i=0
	temp =[]
	for element in similar_sort_movies:
		temp.append(db.new_db.find({}, {"_id": False})[element[0]])
		i+=1
		if(i>10):
			break
	for element in temp:
		movies.append(element["Title"])
		poster.append(element["YouTube Trailer"])
		year.append(element["Year"])
		genre.append(element["Genres"])
		rating.append(element["Rating"])
		summary.append(element["Short Summary"])
			
	return movies,poster,year,genre,rating,summary
