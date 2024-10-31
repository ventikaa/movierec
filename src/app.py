import streamlit as st
import pandas as pd
from data_loader import load_movielens_data
from embedding import generate_movie_embeddings
from recommendation import recommend_movies

def main():
    st.title("Movie Recommendation System")

    # Load data
    ratings, movies = load_movielens_data()
    embeddings = generate_movie_embeddings(movies)

    # User input
    selected_movie = st.selectbox("Select a movie:", movies['title'])
    movie_id = movies[movies['title'] == selected_movie]['movieId'].values[0]

    if st.button("Recommend"):
        recommendations = recommend_movies(movie_id, embeddings, movies)
        st.write("Recommended Movies:")
        for index, row in recommendations.iterrows():
            st.write(f"{row['title']} ({row['genres']})")

if __name__ == "__main__":
    main()
 
