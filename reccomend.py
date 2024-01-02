#import the libraries
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import sigmoid_kernel

#Read the dataset
movie_df=pd.read_csv('data/IMDB-Movie-Data.csv')


#create indices variable
indices=pd.Series(movie_df.index,index=movie_df['Title']).drop_duplicates()


#Access the description column in the dataset
print(movie_df['Description'].head())



#call the tfidf function
tvf= TfidfVectorizer(min_df=3,max_features=None,strip_accents='unicode',analyzer='word',token_pattern=r'\w{1,}',
                     ngram_range=(1,3),
                     stop_words='english')

#Replace null values with empty string
movie_df['Description']=movie_df['Description'].fillna('')

#Apply tfidf on description column
tvf_matrix = tvf.fit_transform(movie_df['Description'])
#call the sigmoid kernel and apply it on tfidf description column
sig=sigmoid_kernel(tvf_matrix,tvf_matrix)

#Then create a reccomendation function 
# #Create a reccomend function
# def reccomend(movie_name,sig=sig):

#   #convert the movie name into index
#   idx=indices[movie_name]

#   #Then give it to the sigmoid function
#   sig_scores=list(enumerate(sig[idx]))

#   #Then arrange the value in descending order
#   sig_scores =sorted(sig_scores,key=lambda x:x[1],reverse=True)

#   #get the top 5 reccomendation
#   sig_scores=sig_scores[0:6]

#   #Get the index of the movie
#   movie_indices=[i[0] for i in sig_scores]

#   #Then return the movie name
#   return movie_df['Title'].iloc[movie_indices]
def reccomend(movie_name, sig=sig):
    # Convert the movie name into index
    idx = indices[movie_name]

    # Then give it to the sigmoid function
    sig_scores = list(enumerate(sig[idx]))

    # Then arrange the value in descending order
    sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)

    # Get the top 5 recommendations
    sig_scores = sig_scores[0:6]

    # Get the index of the movie
    movie_indices = [i[0] for i in sig_scores]

    # Then return the movie names as a list
    return movie_df['Title'].iloc[movie_indices].tolist()


