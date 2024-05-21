import streamlit as st
import pickle
import pandas as pd
import requests

st.set_page_config(layout="wide")

def fetch_poster(movieId):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movieId}?api_key=f2ff3cda6a650b066060fa51ade574f8")
    data = response.json()
    
    poster = data.get('poster_path')
    poster_url = f"https://image.tmdb.org/t/p/w500{poster}" if poster else ""
    return poster_url

def recommend(Movie):
    Movie_index = Movie_df[Movie_df['title'] == Movie].index[0]
    distances = similarity[Movie_index]
    Movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]
    recommended_Movie = []
    recommended_Movie_poster = []
    for i in Movie_list:
        Movie_id = Movie_df.iloc[i[0]].movie_id
        recommended_Movie.append(Movie_df.iloc[i[0]].title)
        recommended_Movie_poster.append(fetch_poster(Movie_id))
    return recommended_Movie, recommended_Movie_poster

# Load the movie data and similarity matrix
Movie_dict = pickle.load(open('Movies.pkl', 'rb'))
Movie_df = pd.DataFrame(Movie_dict)

# Print the columns to verify structure
print("Columns in the DataFrame:", Movie_df.columns)

similarity = pickle.load(open('Classifier.pkl', 'rb'))

st.title('Movie Recommendation System')

selected_Movie_name = st.selectbox('Select a movie you like', Movie_df['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_Movie_name)

    cols = st.columns(3)
    for i in range(len(names)):
        with cols[i % 3]:
            st.text(names[i])
            st.image(posters[i])
