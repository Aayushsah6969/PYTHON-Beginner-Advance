#Movie_Max: A movie recomendation app

import numpy as np

# ------------------------------------
# Step 1: Define Movie Feature Vectors
# ------------------------------------

# Each row is a movie
# Each column is a genre feature: [Action, Comedy, Romance, Horror, Sci-Fi]
movie_features = np.array([
    [5, 1, 1, 0, 4],  # Interstellar
    [4, 1, 1, 0, 5],  # Guardians of Galaxy
    [1, 5, 4, 0, 1],  # Crazy Rich Asians
    [0, 2, 5, 1, 0],  # The Notebook
    [0, 1, 1, 5, 0]   # The Conjuring
])

# List of movie names corresponding to each row
movie_names = [
    "Interstellar",         
    "Guardians of Galaxy",  
    "Crazy Rich Asians",    
    "The Notebook",         
    "The Conjuring"         
]

# ------------------------------------
# Step 2: Define Cosine Similarity Function
'''
Cosine similarity is a metric used to measure how similar two vectors are by calculating the cosine of the angle between them. The result ranges from -1 to 1, where:

1 means the vectors are identical
0 means the vectors are perpendicular
-1 means the vectors are opposite
'''
# ------------------------------------

def cosine_similarity(vec1, vec2):
    """
    Calculates cosine similarity between two vectors.
    """
    dot_product = np.dot(vec1, vec2)            # A · B
    norm_vec1 = np.linalg.norm(vec1)            # ||A||
    norm_vec2 = np.linalg.norm(vec2)            # ||B||
    return dot_product / (norm_vec1 * norm_vec2)

# ------------------------------------
# Step 3: Recommendation Function
# ------------------------------------

def recommend(movie_index, movie_features, movie_names, top_n=3):
    """
    Recommends top N similar movies using cosine similarity.
    """
    # Get the feature vector of the selected movie
    selected_movie = movie_features[movie_index]

    # Create a list to store similarity scores
    similarity_scores = []

    # Loop through all movies
    for i in range(len(movie_features)):
        if i != movie_index:  # Skip the selected movie itself
            other_movie = movie_features[i]
            # Calculate cosine similarity
            similarity_score = cosine_similarity(selected_movie, other_movie)
            # Store the result as a pair: (movie number, similarity)
            similarity_scores.append([i, similarity_score])

    # Sort the list by similarity score (highest first)
    similarity_scores.sort(key=lambda x: x[1], reverse=True)

    # Print the top N similar movies
    print(f"\nTop {top_n} movies similar to '{movie_names[movie_index]}':\n")
    for i in range(top_n):
        movie_num = similarity_scores[i][0]
        score = similarity_scores[i][1]
        print(f"{movie_names[movie_num]} (Similarity: {score:.2f})")

# ------------------------------------
# Step 4: Run the Recommender
# ------------------------------------

# Example: Recommend similar movies to 'Interstellar' (index 0)
recommend(2, movie_features, movie_names, top_n=2)
