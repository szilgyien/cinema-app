from cinema.movies import load_movies, show_movies

def main():
    
    movies = load_movies("data/movies.json")

    if movies:
        show_movies(movies)

if __name__ == "__main__":
    main()