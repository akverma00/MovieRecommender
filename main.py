import requests_with_caching
import json


def get_movies_from_tastedive(word):
    baseurl = "https://tastedive.com/api/similar"
    dic = {}
    dic['q'] = word
    dic['type'] = "movies"
    dic['limit'] = 5
    return requests_with_caching.get(baseurl, params=dic).json()


def extract_movie_titles(word):
    return [x["Name"] for x in word["Similar"]["Results"]]


def get_related_titles(movies):
    l2 = []
    for movie in movies:
        l2 = l2 + [title for title in extract_movie_titles(get_movies_from_tastedive(movie)) if title not in l2]
    return l2


def get_movie_data(movie):
    baseurl = "http://www.omdbapi.com/"
    dic = {}
    dic['t'] = movie
    dic['r'] = 'json'
    return requests_with_caching.get(baseurl, params=dic).json()
