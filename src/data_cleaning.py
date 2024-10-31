import pandas as pd

def clean_movielens_data(ratings, movies):
    """
    Clean the MovieLens data.
    Parameters:
        ratings (DataFrame): User ratings for movies.
        movies (DataFrame): Movie metadata.
    Returns:
        cleaned_ratings (DataFrame): Cleaned user ratings.
        cleaned_movies (DataFrame): Cleaned movie metadata.
    """
    # Convert timestamps to datetime
    ratings['timestamp'] = pd.to_datetime(ratings['timestamp'], unit='s')

    # Remove duplicates
    ratings.drop_duplicates(inplace=True)
    movies.drop_duplicates(inplace=True)

    # Reset index
    cleaned_ratings = ratings.reset_index(drop=True)
    cleaned_movies = movies.reset_index(drop=True)

    return cleaned_ratings, cleaned_movies

if __name__ == "__main__":
    from data_loader import load_movielens_data

    ratings, movies = load_movielens_data()
    cleaned_ratings, cleaned_movies = clean_movielens_data(ratings, movies)

    print("Cleaned Ratings Data:\n", cleaned_ratings.head())
    print("Cleaned Movies Data:\n", cleaned_movies.head())
 
