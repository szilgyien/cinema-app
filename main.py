from cinema.movies import load_movies, show_movies, find_movie_by_id


def main():
    movies = load_movies("data/movies.json")

    if movies:
        show_movies(movies)
        
        try:
            movie_id = int(input("\nEnter the ID of the selected movie: "))
            selected_movie = find_movie_by_id(movies, movie_id)
            
            if selected_movie:
                print(f"\nSuccessfully selected: **{selected_movie['title']}**")
            else:
                print("\nError: No movie found with this ID.")
        except ValueError:
            print("\nError: Please enter a number!")

if __name__ == "__main__":
    main()