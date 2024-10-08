# -*- coding: utf-8 -*-
"""MovieRecommendations.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15MHC4lup5HGKMKm3n1C_HcMB-qku3FED

## Import Libraries
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import os
from math import sqrt
import matplotlib.pyplot as plt
# %matplotlib inline

"""## Mount Drive"""

from google.colab import drive
drive.mount('/content/drive')

"""## Read Data"""

movies = pd.read_csv('/content/drive/MyDrive/MovieLens/movies.csv')
ratings = pd.read_csv('/content/drive/MyDrive/MovieLens/ratings.csv')

"""### Movies"""

movies.head() # Display movies

"""#### Movies Data Shape"""

movies.shape

"""#### Checking Null"""

movies.isnull().sum()

"""#### Check Movies Data"""

movies.describe()

"""### Ratings"""

ratings.head() # Display ratings

"""#### Ratings Data Shape"""

ratings.shape

"""#### Checking Null"""

ratings.isnull().sum()

"""#### Check Ratings Data"""

ratings.describe()

"""## Data Preprocessing

### Make Year Coloumn From Title
"""

movies['year'] = movies.title.str.extract('(\(\d\d\d\d\))',expand=False)
movies['year'] = movies.year.str.extract('(\d\d\d\d)',expand=False)

movies.head()

"""### Deleting Year in Title"""

movies['title'] = movies['title'].str.replace(r'\(\d{4}\)', '', regex=True).str.strip()

movies.head()

"""### Droping Unecessary Column

#### Drop Genres
"""

movies.drop(columns=['genres'], inplace=True) # Drop Genres in Movies
movies.head()

"""#### Drop Timestamps"""

ratings.drop(columns=['timestamp'], inplace=True) # Drop Timestamp in Ratings
ratings.head()

"""The process for creating a user-based recommendation system is as follows :

* Select Users: Choose users who have watched movies.
* Retrieve Viewing Records: Obtain records of the movies watched by these users.
* Calculate Similarity Scores: Compute similarity scores between users based on their movie viewing histories.
* Recommend Items: Recommend movies to users based on the highest similarity scores.

## Modelling & Evaluating

### Select User
"""

# Representing user input data.
user = [
            {'title':'Shutter Island', 'rating':4},
            {'title':'Toy Story', 'rating':2.5},
            {'title':'Home Alone 3', 'rating':3},
            {'title':"Pulp Fiction", 'rating':4.5},
            {'title':'Your Name.', 'rating':5}
         ]
inputMovie = pd.DataFrame(user)
inputMovie

"""### Filter Movie Based on Title"""

# Filter The Input Based on Title
Id = movies[movies['title'].isin(inputMovie['title'].tolist())]
inputMovie = pd.merge(Id, inputMovie)
inputMovie = inputMovie.drop(labels= 'year',axis = 1)
inputMovie

"""### Filter User Based on Movies"""

users = ratings[ratings['movieId'].isin(inputMovie['movieId'].tolist())]
users.head()

"""### Users Shape"""

users.shape

"""### Sub Dataframes

#### Group a DataFrame by userId
"""

userSubsetGroup = users.groupby(['userId'])

userSubsetGroup.get_group(1030) # Example of a group by getting all users of a particular userId

"""### Sort users by similarity to prioritize those with the most similar films

#### Sort a list of user groups based on the number of items each group contains.
"""

userSubsetGroup = sorted(userSubsetGroup,  key=lambda x: len(x[1]), reverse=True)

"""#### Retrieves the first 3 elements from the userSubsetGroup list"""

userSubsetGroup[0:3]

"""#### Limit the size of the userSubsetGroup list to its first 100 elements"""

userSubsetGroup = userSubsetGroup[0:100]

"""### Pearson Correlation

* Store Pearson Correlation in dictionary, where key is user Id and value is coefficient
* Sort the current input and user group so that the values are not mixed up later
* Get review scores for movies
* Store in a deep temporary buffer variable to facilitate future calculations
* Put the current user group reviews in list format
* Calculate pearson correlation between two users, called, x and y
"""

# Initialize an empty dictionary to store Pearson correlation coefficients
pearsonCorDict = {}

# Iterate over groups of users and their movie ratings
for name, group in userSubsetGroup:
    # Sort the group and the input movie data by 'movieId'
    group = group.sort_values(by='movieId')
    inputMovie = inputMovie.sort_values(by='movieId')

    # Get the number of movies in the group
    n = len(group)

    # Filter the input movie data to include only movies that are also in the user's group
    temp = inputMovie[inputMovie['movieId'].isin(group['movieId'].tolist())]

    # Get the list of ratings for the filtered movies
    tempRatingList = temp['rating'].tolist()
    tempGroupList = group['rating'].tolist()

    # Calculate the components of Pearson correlation
    Sxx = sum([i**2 for i in tempRatingList]) - pow(sum(tempRatingList), 2) / float(n)
    Syy = sum([i**2 for i in tempGroupList]) - pow(sum(tempGroupList), 2) / float(n)
    Sxy = sum(i * j for i, j in zip(tempRatingList, tempGroupList)) - sum(tempRatingList) * sum(tempGroupList) / float(n)

    # Compute the Pearson correlation coefficient
    # Ensure that neither Sxx nor Syy is zero to avoid division by zero
    if Sxx != 0 and Syy != 0:
        pearsonCorDict[name] = Sxy / sqrt(Sxx * Syy)
    else:
        pearsonCorDict[name] = 0

"""### Retrieve Items From Dictionary"""

pearsonCorDict.items()

"""### Creates a Dataframe from Dictionary and Reset Index"""

# Convert to DataFrame
pearsonDF = pd.DataFrame.from_dict(pearsonCorDict, orient='index', columns=['similarityIndex'])

# Reset index
pearsonDF['userId'] = pearsonDF.index.map(lambda x: x[0] if isinstance(x, tuple) else x)
pearsonDF.index = range(len(pearsonDF))
pearsonDF.head()

"""### Identify and view the top 50 users with the highest similarity scores from the pearsonDF DataFrame."""

# Sort the DataFrame by 'similarityIndex' in descending order
topUsers = pearsonDF.sort_values(by='similarityIndex', ascending=False)[0:50]

# Display the first 5 rows of the top 50 sorted users
topUsers.head()

"""Take a weighted average of movie ratings using Pearson Correlation as the weight. But to do this, Get the movies watched by the user in our pearsonDF from ratings dataframe and then store the correlation in a new column called _similarityIndex".

### Combines the user similarity information with their ratings data, allowing you to see which movies the top similar users have rated.
"""

# Merge the top 50 users with the ratings DataFrame on the 'userId' column
# This combines user similarity data with their respective ratings
topUsersRating = topUsers.merge(ratings, left_on='userId', right_on='userId', how='inner')

# Display the first 5 rows of the merged DataFrame to preview the combined data
topUsersRating.head()

"""### Multiplying similarity by user's ratings"""

# Calculate the weighted rating for each user
# The weighted rating is computed as the product of 'similarityIndex' and 'rating'
topUsersRating['weightedRating'] = topUsersRating['similarityIndex'] * topUsersRating['rating']

# Display the first 5 rows of the DataFrame with the new 'weightedRating' column
topUsersRating.head()

"""### Apply sum to topUsers after grouping them by userId"""

# Group the top users' ratings by 'movieId' and sum the similarity index and weighted ratings for each movie
tempTopUsersRating = topUsersRating.groupby('movieId').sum()[['similarityIndex', 'weightedRating']]

# Rename the columns for better clarity
tempTopUsersRating.columns = ['sum_similarityIndex', 'sum_weightedRating']

# Display the first few rows of the resulting DataFrame
tempTopUsersRating.head()

"""## Recommendations

### Create empty dataframe to take the weighted average
"""

# Create an empty DataFrame to store the recommendation results
recommendation_df = pd.DataFrame()

# Calculate the weighted average recommendation score for each movie
# This is done by dividing the sum of weighted ratings by the sum of similarity indices
recommendation_df['weighted average recommendation score'] = tempTopUsersRating['sum_weightedRating'] / tempTopUsersRating['sum_similarityIndex']

# Add the 'movieId' as a column to the DataFrame
recommendation_df['movieId'] = tempTopUsersRating.index

# Display the first few rows of the recommendation DataFrame
recommendation_df.head()

"""### Sort and Display top 10 Movies from Dataframes Based On Their Recommendation Scores."""

recommendation_df = recommendation_df.sort_values(by='weighted average recommendation score', ascending=False)
recommendation_df.head(10)

"""### Get the top 10 movies with the highest recommendation score. These are the top 10 recommendations for input users based on what others are watching"""

movies.loc[movies['movieId'].isin(recommendation_df.head(10)['movieId'].tolist())]