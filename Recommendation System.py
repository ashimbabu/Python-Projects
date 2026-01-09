print("===== Recommendation System =====")

# Movie database (content-based)
movies = {
    "Inception": ["Sci-Fi", "Action", "Thriller"],
    "Interstellar": ["Sci-Fi", "Drama"],
    "The Dark Knight": ["Action", "Crime"],
    "Avengers": ["Action", "Sci-Fi"],
    "Titanic": ["Romance", "Drama"],
    "Notebook": ["Romance", "Drama"],
    "Joker": ["Crime", "Drama", "Thriller"],
    "Matrix": ["Sci-Fi", "Action"]
}

def get_user_preferences():
    print("\nAvailable Genres:")
    genres = set()
    for g in movies.values():
        genres.update(g)

    for genre in sorted(genres):
        print("-", genre)

    user_input = input("\nEnter preferred genres (comma separated): ")
    return [g.strip() for g in user_input.split(",")]

def similarity(movie_genres, user_genres):
    return len(set(movie_genres) & set(user_genres))

def recommend(user_genres):
    scores = {}

    for movie, genres in movies.items():
        score = similarity(genres, user_genres)
        if score > 0:
            scores[movie] = score

    recommendations = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return recommendations

def main():
    user_genres = get_user_preferences()
    recommendations = recommend(user_genres)

    if recommendations:
        print("\n🎬 Recommended Movies:")
        for movie, score in recommendations:
            print(f"{movie} (match score: {score})")
    else:
        print("No recommendations found.")

main()
