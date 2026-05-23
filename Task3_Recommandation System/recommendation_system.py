import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_csv(r"C:\Users\S Maruthi Rao\Desktop\Codsoft\Task3\movies.csv")

# Convert genre text into vectors
cv = CountVectorizer()
matrix = cv.fit_transform(movies['genre'])

# Calculate similarity
similarity = cosine_similarity(matrix)

# Recommendation function
def recommend(movie_name):
    movie_name = movie_name.lower()

    # Find movie index
    movie_index = None

    for i in range(len(movies)):
        if movies.iloc[i]['title'].lower() == movie_name:
            movie_index = i
            break

    if movie_index is None:
        print("Movie not found.")
        return

    # Get similarity scores
    scores = list(enumerate(similarity[movie_index]))

    # Sort movies
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print("\nRecommended Movies:\n")

    count = 0
    for movie in sorted_scores[1:]:
        index = movie[0]
        print(movies.iloc[index]['title'])
        count += 1

        if count == 5:
            break

# User Input
movie = input("Enter a movie name: ")

recommend(movie)