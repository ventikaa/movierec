import pandas as pd

def load_movielens_data():
    """
    Load MovieLens 25M dataset.
    Returns:
        ratings (DataFrame): User ratings for movies.
        movies (DataFrame): Movie metadata.
    """
    ratings = pd.read_csv('data/ml-25m/ratings.dat', sep='::', header=None, names=['userId', 'movieId', 'rating', 'timestamp'], engine='python')
    movies = pd.read_csv('data/ml-25m/movies.dat', sep='::', header=None, names=['movieId', 'title', 'genres'], engine='python')

    return ratings, movies

if __name__ == "__main__":
    ratings, movies = load_movielens_data()
    print("Ratings Data:\n", ratings.head())
    print("Movies Data:\n", movies.head())
