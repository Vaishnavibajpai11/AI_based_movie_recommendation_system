# AI_based_movie_recommendation_system

Overview
This project is an interactive movie recommendation system built using Python, Pandas, Scikit-learn, and Streamlit. It allows users to discover movies similar to their favourites based on content similarity, providing a simple, intuitive, and visually appealing interface.
The system uses a content-based filtering approach, analyzing features like movie title, genres, keywords, cast, and crew to recommend similar movies.

**Features**
-> Search by Movie Name – Type or select a movie from the dataset to get recommendations
-> Top Recommendations – Shows 5 movies most similar to the input
-> Customizable UI – Built with Streamlit with layout for an interactive experience
-> Data-driven – Uses movies.csv and credits.csv datasets to create the recommendation model
-> Reusable Model – Saved similarity matrix and processed dataset in .pkl files for faster loading

**Technology Stack**
-> Python 3 – Data processing and backend logic
-> Pandas – Data cleaning and manipulation
-> Scikit-learn – Content-based similarity computation
-> Streamlit – Interactive web interface
-> Pickle – Save and load processed datasets and similarity matrix

**How It Works**
-> Preprocesses the dataset (movies.csv + credits.csv) by combining features like genres, keywords, cast, and crew into a single tags column.
-> Converts text features into vector embeddings using CountVectorizer.
-> Computes cosine similarity between movies based on these embeddings.
-> Provides an interface where users can input a movie and get a list of top 5 similar movies instantly.

**Dataset**
movies.csv – Movie information including title, overview, genres, etc.
credits.csv – Cast and crew information

