# Movie Recommendation System - Jericho Luthfi Syahli

## Project Overview

In the rapidly expanding movie industry, selecting what to watch next can be overwhelming due to the vast number of options available. This project aims to tackle this issue by developing a movie recommendation system that aligns with user preferences. We will employ Collaborative Filtering (CF) to achieve this. Collaborative Filtering predicts user preferences by analyzing historical ratings from users, allowing us to recommend movies based on similar users’ preferences.

## Business Understanding

### Problem Statements
- **User Challenge**: Users often struggle to decide what movie to watch next due to the sheer volume of choices available.
- **Business Challenge**: How can we effectively suggest movies to users in a way that aligns with their individual tastes and preferences?

### Goals
- **Business Goal**: Enhance user engagement and satisfaction by providing personalized movie recommendations.
- **Technical Goal**: Implement a Collaborative Filtering method to predict user preferences and generate movie recommendations.

## Data Understanding

We are using the MovieLens 32M dataset, which includes over 32 million movie ratings from users. The dataset comprises information on movie titles, genres, ratings, and user IDs. For this project, we will use the `movies.csv` and `ratings.csv` files. The MovieLens dataset can be downloaded from [here](https://grouplens.org/datasets/movielens/).

### movies.csv

 ![gambar](https://github.com/user-attachments/assets/09415da6-bafe-4327-9fee-a015ceae6b14)


- **movieId**: Unique identifier for each movie.
- **title**: Title of the movie.
- **genres**: Genres associated with the movie.

### ratings.csv

![gambar](https://github.com/user-attachments/assets/ff1504d8-a1db-4094-9c06-5853701737d9)


- **userId**: Unique identifier for each user.
- **movieId**: Unique identifier for each movie.
- **rating**: Rating given by the user.
- **timestamp**: Date and time when the rating was given.

## Data Preparation

The data preparation steps include:
1. **Importing Libraries**: Load necessary libraries for data manipulation and analysis.
2. **Loading Data**: Import the `movies.csv` and `ratings.csv` files.
3. **Data Cleaning**:
   - Extract the year from the movie title.
   - Remove the year from the movie title column.
   - Drop unnecessary columns from the datasets ( timestamps and genres).

## Modeling

### User-Based Recommendation System

1. **Data Segmentation**:
   - Create sub-dataframes based on user ratings. Each sub-dataframe contains ratings from a specific user.
   - Example: Create a dataframe with columns for `userId`, `movieId`, and `rating`.

3. **Similarity Calculation**:
   - **Pearson Correlation**: Calculate the Pearson Correlation coefficient between users to determine similarity.
   - **Sample Calculation**: For a given user, retrieve ratings from similar users and compute the similarity scores.

4. **Generating Recommendations**:
   - **Weighted Average Calculation**: Compute the weighted average of movie ratings using similarity scores as weights.
   - **Top-N Recommendations**: Aggregate results to identify the top 10 movies with the highest recommendation scores.

5. **Data Aggregation**:
   - Format the aggregated data to list recommendations for the user.
   - Example: Store recommendations in a DataFrame and sort by recommendation score.

## Recommendations Results

Based on user input and ratings from similar users, the top 10 recommended movies are:

![Top 10 Recommendations](https://github.com/user-attachments/assets/ebff6d99-f849-44c3-a4bd-1db4ce1e0573)

## Evaluation

![gambar](https://github.com/user-attachments/assets/972d4b2f-6778-4271-824c-02ea48e665bc)

To evaluate the recommendation system, we used the **Pearson Correlation** metric, which measures the linear correlation between user ratings. The recommendations were assessed based on this correlation, resulting in a weighted average score for each movie. The system successfully provided high-quality suggestions, with scores reaching up to **5.0**, indicating effective alignment with user preferences.
