from numpy.lib.function_base import diff
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import difflib

def get_index_from_title(title):
	movies_title_list =df['Title'].tolist()
	common_title =difflib.get_close_matches(title, movies_title_list,1)
	title_sim =common_title[0]
	return df[df.Title == title_sim]["Index"].values[0]

def get_rating_from_index(index):
	return df[df.Index == index]["Rating"].values[0]

def get_trailer_from_index(index):
	return df[df.Index == index]["YouTube Trailer"].values[0]	

def get_summary_from_index(index):
	return df[df.Index == index]["Short Summary"].values[0]

def get_genre_from_index(index):
	return df[df.Index == index]["Genres"].values[0]

def get_year_from_index(index):
	return df[df.Index == index]["Year"].values[0]

def get_title_from_index(index):
	return df[df.Index == index]["Title"].values[0]


##	Step 1: Read CSV File	##
df = pd.read_csv("dataset.csv")
##	Step 2: Cleaning Dataset##
df['Cast'] = df['Cast'].str.replace('|',' ',regex=True)
df['Writers'] =df['Writers'].str.replace('|',' ',regex=True)
items = ['Title','Genres','Director','Cast','Writers']

for feature in items:
	df[feature] = df[feature].fillna("")
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
def func(input_movies):
	
	df["combined_features"] = df.apply(combine_items,axis=1)
	movie_index = get_index_from_title(input_movies)

	cv = CountVectorizer()

	count_matrix = cv.fit_transform(df["combined_features"])
	cosine_sim = cosine_similarity(count_matrix) 

	similar_movie_list =  list(enumerate(cosine_sim[movie_index]))
	similar_sort_movies = sorted(similar_movie_list,key=lambda x:x[1],reverse=True)
	
	i=0
	year =[]
	poster =[]
	movies = []
	genre =[]
	rating =[]
	summary =[]

	for element in similar_sort_movies:
			if i>10:
				break	
			movies.append(get_title_from_index(element[0]))
			poster.append (get_trailer_from_index(element[0]))
			year.append (get_year_from_index(element[0]))
			genre.append (get_genre_from_index(element[0]))
			rating.append (get_rating_from_index(element[0]))
			summary.append (get_summary_from_index(element[0]))
			i+=1
			
	return movies,poster,year,genre,rating,summary
