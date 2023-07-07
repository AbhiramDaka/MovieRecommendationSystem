import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
    data=requests.get(url)
    data=data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path

def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommend_movie=[]
    recommend_poster=[]
    for i in distance[0:8]:
        movies_id=movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movie, recommend_poster

# Load pickle files
movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list=movies['title'].values

# Streamlit app
st.header("Movie Recommendation System: Your Ultimate Movie Recommender")
image = open('img.jpg', 'rb')
image_bytes = image.read()
st.image(image_bytes, use_column_width=True)

selectvalue = st.selectbox("Select what are you looking for", movies_list)

if st.button("Search"):
    movie_name, movie_poster = recommend(selectvalue)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image(movie_poster[0])
        st.text(movie_name[0])
    with col2:
        st.image(movie_poster[1])
        st.text(movie_name[1])
    with col3:
        st.image(movie_poster[2])
        st.text(movie_name[2])
    with col4:
        st.image(movie_poster[3])
        st.text(movie_name[3])

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image(movie_poster[4])
        st.text(movie_name[4])
    with col2:
        st.image(movie_poster[5])
        st.text(movie_name[5])
    with col3:
        st.image(movie_poster[6])
        st.text(movie_name[6])
    with col4:
        st.image(movie_poster[7])
        st.text(movie_name[7])
