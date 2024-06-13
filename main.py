import tkinter as tk
from tkinter import ttk
import pandas as pd

# Load movie titles from CSV file
import backend

def load_movies():
    movies = pd.read_csv(r'data/movies.csv', sep=';')
    movies_df = pd.DataFrame(movies, columns=['title'])
    x = []
    for index, row in movies_df.iterrows():
        y = row['title'].split(' (')
        y = y[0].split(',')
        x.append(y[0].lower())

    movies_df['title'] = x
    movies = movies_df["title"].tolist()
    return movies

def process_choice():
    selected_method=method.get()
    N=int(similar_movies_entry.get())
    movies=[]
    if selected_method == "Based on cateogry":
        movies=backend.recommend_by_movies(movie.get(),N)
    if selected_method == "Based on user":
        movies=backend.recommend_by_movie2(movie.get(),N)
    if selected_method == "Based on catogery and user":
        movies=backend.recommend_by_user(int(user_id_entry.get()),N
                                             )
    display_movies(movies)

def display_movies(movies):
    movie_list = "\n".join(movies)
    movie_label.config(text=movie_list)


# Create GUI
root = tk.Tk()
root.geometry("400x400")

# Create combo boxes
method = tk.StringVar()
movie = tk.StringVar()

# Create user ID entry box
user_id_label = ttk.Label( text="Enter the user ID:")
user_id_entry = ttk.Entry()

user_id_label.grid(row=5,column=0,pady=5)
user_id_entry.grid(row=5,column=20,pady=5)

method_label = ttk.Label(text="Select a recommendation method:")
method_label.grid(row=25,column=0,pady=5)
method_box = tk.ttk.Combobox(root, textvariable=method, values=["Based on cateogry", "Based on user" , "Based on catogery and user"])
method_box.grid(row=25,column=20,pady=5)

movie_title_label = ttk.Label(text="Select a  movie")
movie_title_label.grid(row=45,column=0,pady=5)
movie_box = tk.ttk.Combobox(root, textvariable=movie, values=load_movies())
movie_box.grid(row=45,column=20,pady=5)

similar_movies_label = ttk.Label(text="Enter number of similar movies:")
similar_movies_entry = ttk.Entry()

similar_movies_label.grid(row=65,column=0,pady=5)
similar_movies_entry.grid(row=65,column=20,pady=5)

apply_button = ttk.Button(root, text="Show Similar Movies", command=process_choice)
apply_button.grid(column=0,pady=5)

movie_label = ttk.Label(root, text="")
movie_label.grid(column=0,pady=5)

root.mainloop()