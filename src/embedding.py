import pandas as pd
from sentence_transformers import SentenceTransformer

def generate_movie_embeddings(movies):
    """
    Generate embeddings for movie titles and genres.
    Parameters:
        movies (DataFrame): DataFrame containing movie metadata.
    Returns:
        embeddings (numpy.ndarray): Array of embeddings for each movie.
    """
    model = SentenceTransformer('all-MiniLM-L6-v2')  # Load pre-trained model
    movie_descriptions = movies['title'] + " " + movies['genres']  # Combine title and genres
    embeddings = model.encode(movie_descriptions.tolist(), show_progress_bar=True)

    return embeddings

if __name__ == "__main__":
    from data_loader import load_movielens_data

    ratings, movies = load_movielens_data()
    embeddings = generate_movie_embeddings(movies)
    print("Generated Movie Embeddings:\n", embeddings)
 
