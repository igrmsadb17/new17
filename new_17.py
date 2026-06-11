
 # using movie_index find similarity array from similarity_matrix
    # use enumerate to have : index_of_movie, similarity_values
    # convert to list
    # use sorted(reverse = True, lambda x : x[1])
    # becoz of enumerate 2 values are present for each movie in list. 1st is index, 2nd is similarity value. 
    # we need to order the movies on the basis of similarity value. use lambda x : x[1], which tells to not choose index and choose similarity value
    # revserse = True -> orders the values from highest to lowest
    # take only 5 movie name: slice method -> [1:6]

import streamlit as st
import pickle
import requests

st.title("Movie Recommendation System")

movies_df = pickle.load(open("movies.pkl","rb"))
movie_titles = movies_df["title"]

movie_name = st.selectbox("Select Movie: ", movie_titles)

similarity_matrix = pickle.load(open("similarity.pkl", "rb"))

def poster_url(movie_id):
    api_key = st.secrets["TMDB_API_KEY"]
    search_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    response = requests.get(search_url).json()

    base_url = f"https://image.tmdb.org/t/p/"
    image_size = "w500"
    poster_path = response["poster_path"]
    if poster_path:
        path_url = base_url + image_size + poster_path
        return path_url
    
    return None


def recommendations(movie_name):
    movie_names = []
    poster_urls = []
    movie_index= movies_df[movies_df["title"] == movie_name].index[0]

    
    similarity_list = sorted(list(enumerate(similarity_matrix[movie_index])), reverse = True, key = lambda x : x[1])[1:6]
    for i in similarity_list:
        # i[0] represents index value in similarity_list.
        # for e.g.: x = [(0,1), (12, 0.98), (31, 0.65)]. let's consider x as a similarity array
        # for i in x: means i at a time going to store (0,1) then (12, 0.98) then (31, 0.65)
        # i[0] means 0 from (0,1), 12 from (12, 0.98), and 31 from (31, 0.65). here, 0, 12, and 31 are indices of movies
        # movies_df.iloc[i[0]]["title"]: here, if i[0] == 1, then this syntax means lock 1st index'd movie's row then give it's title
        movie_names.append(movies_df.iloc[i[0]]["title"])
        poster_urls.append(poster_url(movies_df.iloc[i[0]]["id"]))
    return movie_names, poster_urls

cols = st.columns(5)
names, posters = recommendations(movie_name)

if st.button("Recommendations", width="stretch"):
    for i in range(len(names)):
        with cols[i]:
            st.image(posters[i])
            st.write(names[i])
    





