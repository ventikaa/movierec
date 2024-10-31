import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def recommend_movies(movie_id, movie_embeddings, movies, top_n=5):
    """
    Recommend movies based on the provided movie ID using cosine similarity.
    Parameters:
        movie_id (int): The ID of the movie to find recommendations for.
        movie_embeddings (numpy.ndarray): Array of movie embeddings.
        movies (DataFrame): DataFrame containing movie metadata.
        top_n (int): Number of top recommendations to return.
    Returns:
        recommended_movies (DataFrame): DataFrame of recommended movies.
    """
    # Find the index of the movie
    idx = movies[movies['movieId'] == movie_id].index[0]

    # Calculate cosine similarity
    sim_scores = cosine_similarity(movie_embeddings[idx].reshape(1, -1), movie_embeddings).flatten()

    # Get the indices of the top_n most similar movies
    top_indices = sim_scores.argsort()[-top_n-1:-1][::-1]

    recommended_movies = movies.iloc[top_indices]
    return recommended_movies

if __name__ == "__main__":
    from data_loader import load_movielens_data
    from embedding import generate_movie_embeddings

    ratings, movies = load_movielens_data()
    embeddings = generate_movie_embeddings(movies)

    movie_id_to_recommend = 1  # Example movie ID
    recommendations = recommend_movies(movie_id_to_recommend, embeddings, movies)
    print("Recommended Movies:\n", recommendations)
 
