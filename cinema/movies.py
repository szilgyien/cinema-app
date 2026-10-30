import json

def load_movies(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        return []


def show_movies(movies):
    print("=== AVAILABLE MOVIES ===")
    print()
    for movie in movies:
        print(f"{movie['id']}. {movie['title']} | {movie['genre']} | {movie['duration']} min | {movie['ticket_price']} Ft")
        
def find_movie_by_id(movies, movie_id):
    for movie in movies:
        if movie.get('id') == movie_id:
            return movie
    return None