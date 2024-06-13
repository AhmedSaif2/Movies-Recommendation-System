import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

movies =pd.read_csv(r'data/movies.csv', sep=';')
movies_df = pd.DataFrame(movies,columns=['movieId','title','genres'])


ratings =pd.read_csv(r'data/ratings.csv', sep=';')
ratings_df = pd.DataFrame(ratings)

users =pd.read_csv(r'data/users.csv', sep=';')
users_df = pd.DataFrame(users)

#movie_D_F preprossing
x=[]
for index, row in movies_df.iterrows():
    y= row['title'].split(' (')
    y= y[0].split(',')
    x.append(y[0].lower())


movies_df['title']=x
movies_df['genres'] = movies_df['genres'].map(lambda x: x.split('|'))

movies_df['Bag_of_words'] = ''
column='genres'
geners=[]
for index, row in movies_df.iterrows():
    words = ''
    words += ' '.join(row[column]) + ' '
    geners.append(words)

movies_df['Bag_of_words']=geners
df = movies_df[['title','Bag_of_words']]

count1 = CountVectorizer()
count_matrix1 = count1.fit_transform(df['Bag_of_words'])

similarity1 = cosine_similarity(count_matrix1, count_matrix1)

indices = pd.Series(df['title'])


def recommend_by_movies(title, N):
    recommended_movies = []
    idx = indices[indices == title].index[0]
    score_series = pd.Series(similarity1[idx]).sort_values(ascending=False)
    top_N_indices = score_series.iloc[0:].index

    for i in top_N_indices:
        title = get_max_rate_movie(df2['userId'][i])

        if len(recommended_movies) == N:
            break
        if i == idx or title in recommended_movies:
            continue

        recommended_movies.append(df['title'][i])
    return recommended_movies


users_df['Bag_of_words'] = ''
columns = ['gender', 'age', 'occupation']
persons = []
for index, row in users_df.iterrows():
    words = ''
    if row['gender'] == 'F':
        row['gender'] = 1
    else:
        row['gender'] = -1

    for col in columns:
        words += (str(row[col])) + ' '
    persons.append(words)

users_df['Bag_of_words'] = persons
df2 = users_df[['userId', 'Bag_of_words']]

count = CountVectorizer()
count_matrix = count.fit_transform(df2['Bag_of_words'])
similarity = cosine_similarity(count_matrix, count_matrix)
indices_user_id = pd.Series(df2['userId'])

def get_max_rate_movie(user_id):
    recommended_movie=''
    movie_id = ratings_df.loc[(ratings_df['userId']==user_id) & (ratings_df.rating==ratings_df.rating.max()), 'movieId'].iloc[0]
    recommended_movie = movies_df.loc[movies_df['movieId'] == movie_id, 'title'].iloc[0]
    return recommended_movie

def get_max_rate_users(movie_id):
    users = ratings_df.loc[(ratings_df['movieId']==movie_id) & (ratings_df.rating==ratings_df.rating.max()), 'userId'].iloc[0:100]
    recommended_user=[]
    for user_id in users:
        recommended_user.append(users_df.loc[users_df['userId'] == user_id, 'userId'].iloc[0])
    return recommended_user


def recommend_by_user(userId, N):
    recommended_movies = []
    idx = indices_user_id[indices_user_id == userId].index[0]
    score_series = pd.Series(similarity[idx]).sort_values(ascending=False)
    top_N_indices = score_series.iloc[0:].index

    for i in top_N_indices:
        title = get_max_rate_movie(df2['userId'][i])

        if len(recommended_movies) == N:
            break
        if i == idx or title in recommended_movies:
            continue
        recommended_movies.append(title)
    return recommended_movies

def recommend_by_movie2(movie,N):
    movie_id=movies_df.loc[(movies_df['title']==movie) , 'movieId'].iloc[0]
    users=get_max_rate_users(movie_id)
    recommended_movies=[]
    for user_id in users:
        title = get_max_rate_movie(user_id)
        if len(recommended_movies)==N:
            break
        if title in recommended_movies:
            continue
        recommended_movies.append(title)
    return recommended_movies
