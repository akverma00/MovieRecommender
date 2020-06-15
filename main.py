import requests_with_caching
import json


def get_movies_from_tastedive(word):
    baseurl = "https://tastedive.com/api/similar"
    dic = {}
    dic['q'] = word
    dic['type'] = "movies"
    dic['limit'] = 5
    return requests_with_caching.get(baseurl, params=dic).json()

