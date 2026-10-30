import json

def load_movies(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Hiba: A fájl nem található: {file_path}")
        return []

def show_movies(movies):
    print("=== AVAILABLE MOVIES ===")
    print()
    for movie in movies:
        print(f"{movie['id']}. {movie['title']} | {movie['genre']} | {movie['duration']} min | {movie['ticket_price']} Ft")

if __name__ == "__main__":
    movies = load_movies("data/movies.json")
    if movies:
        show_movies(movies)