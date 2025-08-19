#!/bin/python3

from movies_data import csv_data

def recommend_movie(genre):
    movies = {}
    lines = csv_data.strip().split('\n')
    for line in lines[1:]:
        g, m = line.split(',', 1)
        g = g.lower()
        movies.setdefault(g, []).append(m)

    if genre in movies:
        print("Based on your preference for ", genre, "we recommend these movies:")
        for movie in movies[genre]:
            print("- ", movie)
    else:
        print("Sorry, we don't have recommendations for that genre.")

user_genre = input("Enter your favorite genre (e.g. action, comedy, drama, sci-fi, horror, romance, thriller): ").lower()
recommend_movie(user_genre)
