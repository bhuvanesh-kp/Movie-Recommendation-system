import pickle
import streamlit as st
import requests


def fetch_poster(movie_id):
    url='https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc' \

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x:x[1])
    recommended_movies_name =[]
    recommended_movies_poster=[]
    for i in distance[1:6]:
        movie_id = movies.iloc[i[0]]['movie_id']
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies_poster.append(movies.iloc[i[0]].title)
    return recommended_movies_name,recommended_movies_poster

st.header("Movies Recommendation System Using machine learning")
movies = pickle.load(open("artifacts/movie_list.pkl",'rb'))
similarity = pickle.load(open("artifacts/similarity_list.pkl",'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    'Type or select a movie to get recommendation',
    movie_list
)

if st.button('show recommendation'):
    recommended_movies_name , recommended_movies_poster = recommend(selected_movie)