# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    movie_titles = [
        "Forrest Gump",
        "Howl's Moving Castle",
        "No Country for Old Men"
    ]

    movie_directors = [
        "Robert Zemeckis",
        "Hayao Miyazaki",
        "Joel and Ethan Coen"
    ]

    movies = list(zip(movie_titles, movie_directors))

    for title, director in movies:
        print(f"{title} by {director}.")

    movies_list = list(movies)

    print(f"There are {len(movies_list)} movies in the collection.")
    print(f"These are our movies: {movies_list}.")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
