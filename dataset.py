import pandas as pd
import numpy as np
#create a function for generating top 100 movie list
def popular_movies():
    ##read the dataframe
    movies_df=pd.read_csv(r'data/IMDB-Movie-Data.csv')

    #create a dataframe which will contain Title and Rating
    desired_data = movies_df[['Title', 'Rating']]

    #Get the movies whose rating is more then 7.5
    popular_movie_df=desired_data[desired_data['Rating']>=7.9]

    #Then sort them in descending order
    popular_movie_df=popular_movie_df.sort_values(by='Rating',ascending=False)

    #Then return the 
    return popular_movie_df

