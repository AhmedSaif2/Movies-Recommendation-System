# Movie Recommender System using NLP
## Description
This project implements a movie recommender system using Natural Language Processing (NLP) techniques. The system suggests movies to users based on movie's cateogries and user preferences. It utilizes a dataset of users and movie categories and to build a recommendation model that matches users with movies they are likely to enjoy.

## Features
- NLP-based Recommendation: Uses NLP techniques to analyze movie plot summaries and recommend similar movies.
- User Interface: Provides a command-line interface for users to input preferences and receive movie recommendations.
- Dataset Integration: Incorporates a dataset of movie plot summaries to train and validate the recommendation algorithm.

## Technologies Used
- Python
- scikit-learn for machine learning algorithms
- Pandas for data manipulation
- Tkinter for user interface

## Installation
Clone the repository:

```bash
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
```
Install dependencies:

```bash
pip install scikit-learn
pip install pandas
pip install tk
```

## Usage
To run the movie recommender system, use the following command:
```bash
python main.py
```
## Screenshot
Enter the user ID, select a movie, select the recommendation technique (category, user preferences, or both), and indicate how many similar movies you wish to appear.

![image](https://github.com/AhmedSaif2/Movies-Recommendation-System/assets/99100926/36daac03-2293-4810-a45b-f04cb74aba4e)
![image](https://github.com/AhmedSaif2/Movies-Recommendation-System/assets/99100926/4e7c5895-6284-4438-9d7a-5416ebfc3852)


## Dataset
The recommendation model is trained on a dataset of movie plot summaries. This dataset is used to extract features for similarity calculations between movies.
the csv files could be found on the data folder

## Future Improvements
- Develop a web interface using Flask for easier user interaction.
- Enhance NLP algorithms to improve the accuracy of movie suggestions.
