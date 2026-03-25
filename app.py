import pickle
import streamlit as st
import requests
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

api_key = st.secrets["TMDB_API_KEY"]

def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US'
    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        poster_path = data.get('poster_path')

        if poster_path:
            return 'https://image.tmdb.org/t/p/w500/' + poster_path
        else:
            return 'https://via.placeholder.com/500x750?text=No+Image'

    except:
        return 'https://via.placeholder.com/500x750?text=Error'

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x:x[1])
    recommended_movies_name = []
    recommended_movies_poster = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]]['movie_id']
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies_name.append(movies.iloc[i[0]].title)
    return recommended_movies_name, recommended_movies_poster

st.header('Movies Recommendation System Using Machine Learning')
movies = pickle.load(open('artificates/movie_list.pkl', 'rb'))

cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()

similarity = cosine_similarity(vectors)

movie_list = movies['title'].values
selected_movie = st.selectbox(
    'Type or select a movie to get recommendation',
    movie_list
)

if st.button('Show recommendation'):
    recommended_movies_name, recommended_movies_poster = recommend(selected_movie)
    col= st.columns(5)
    for i in range(5):
        with col[i]:
            st.text(recommended_movies_name[i])
            st.image(recommended_movies_poster[i], width=200)
    