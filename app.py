import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="Movie Recommender", layout="wide")

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Function
def recommend(movie):
    movie = movie.lower()
    matches = movies[movies['title'].str.lower().str.contains(movie)]
    
    if matches.empty:
        return ["Movie not found 😢"]
    
    movie_index = matches.index[0]
    distances = similarity[movie_index]
    
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    return [movies.iloc[i[0]].title for i in movies_list]

# UI Design
st.title("🎬 Movie Recommendation System")
st.markdown("### Discover movies similar to your favorite ones!")

col1, col2 = st.columns([2, 1])

with col1:
    movie_name = st.text_input("Enter a movie name")

with col2:
    st.write("")
    st.write("")
    recommend_btn = st.button("🎯 Recommend")

if recommend_btn:
    results = recommend(movie_name)
    
    st.subheader(" Recommended Movies:")
    
    for movie in results:
        st.markdown(f"🎞️ **{movie}**")