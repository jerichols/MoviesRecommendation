# Movie Recommendation System - Jericho Luthfi Syahli

## Project Overview

The movie business has grown quickly, and there are now a huge variety of films to choose from. Choosing what to watch next might be difficult for viewers with so many options. By creating a recommendation system that makes movie recommendations based on user tastes, this project seeks to solve this problem. We'll make advantage of Collaborative Filtering (CF), a method that forecasts user preferences by analyzing user evaluations from the past.

## Business Understanding

### Problem Statements
- How can we recommend movies to users based on their preferences?

### Goals
- Implement a Collaborative Filtering method to recommend movies to users.

## Data Understanding

We are using the MovieLens 32M dataset, which contains over 32 million movie ratings from users. This dataset includes information on movie titles, genres, ratings, and user IDs. The dataset can be downloaded from [here](https://grouplens.org/datasets/movielens/). For this project, we will use the movies.csv and ratings.csv files.

Here is a preview of the movies.csv file:

![gambar](https://github.com/user-attachments/assets/ad02ec90-ce09-4660-bd50-44be08009a3f)

### Explanation of movies.csv
- **movieId**: Unique identifier for each movie.
- **title**: Title of the movie.
- **genres**: Genres associated with the movie.

Here is a preview of the ratings.csv file:

![gambar](https://github.com/user-attachments/assets/c2b979b1-f50c-4666-b755-ccb4193b7598)


### Explanation of ratings.csv
- **userId**: Unique identifier for each user.
- **movieId**: Unique identifier for each movie.
- **rating**: Rating given by the user.
- **timestamp**: Date and time when the rating was given.

## Data Preparation

The data preparation steps for this project include:
- Importing necessary libraries.
- Loading the dataset files.
- Extracting the year from the movie title.
- Removing the year from the movie title column.
- Dropping unnecessary columns from the datasets.
- Building a User-Based Recommendation System:
  - Selecting users based on movies they have watched. User Input :
   
![gambar](https://github.com/user-attachments/assets/6945201c-215d-4009-8a41-2e144cf7ce0f)

  - Retrieving ratings of movies watched by users. Here is the movies watched : 
    
 ![gambar](https://github.com/user-attachments/assets/9c5f3e9e-3792-4b78-aa30-7602a789de6c)

  - Calculating similarity scores.
  - Recommending movies with the highest similarity scores.
- Filtering movies by title and merging data to obtain movie IDs.
- Filtering users who have watched movies in the input and storing the results.

## Modeling

The modeling steps are as follows:
- Creating several sub-dataframes where each has the same value in specified columns.
- Demonstrating a sample group by retrieving all users with a specific userId.
- Sorting users to prioritize those whose movies are most similar to the input.
- Storing Pearson Correlation coefficients in a dictionary, with user IDs as keys and coefficients as values.
- Sorting input data and user groups to prevent mixing of values.
- Retrieving movie review scores.
- Storing data in temporary variables to facilitate future calculations.
- Formatting user group reviews as a list.
- Calculating Pearson Correlation between two users.
- Computing the weighted average of movie ratings using Pearson Correlation as weights.
- Multiplying similarity scores by user ratings.
- Aggregating results to compute top recommendations.
- Creating an empty DataFrame and continuously calculating the weighted average.
- Extracting the top 10 movies with the highest recommendation scores.


### Recommendations Results

Here is a snapshot of the top 10 recommended movies based on user input and ratings from other users:

![gambar](https://github.com/user-attachments/assets/cd2f39e3-cd14-4148-8cfd-34a7fda8b82f)


## Evaluation

![gambar](https://github.com/user-attachments/assets/26a38c78-eb9e-4251-9f52-1a61b51c9c25)

The linear link between user ratings is evaluated using the **Pearson Correlation** evaluation measure. A weighted average recommendation score can be computed by utilizing Pearson Correlation. With a maximum score of **5.0**, the recommendation score that is produced offers a high-quality suggestion.


