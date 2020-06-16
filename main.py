import requests
import json


def get_movies_from_tastedive(word):
    baseurl = "https://tastedive.com/api/similar"
    dic = {}
    dic['q'] = word
    dic['type'] = "movies"
    dic['limit'] = 5
    return requests.get(baseurl, params=dic).json()


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
    dic['apikey'] = "abff2e05"
    dic['t'] = movie
    dic['r'] = 'json'
    return requests.get(baseurl, params=dic).json()


def get_movie_rating(movdat):
    # print (movdat)
    tomdat = [rat['Value'] for rat in movdat['Ratings'] if rat['Source'] == 'Rotten Tomatoes']
    if len(tomdat) is 0:
        val= 0
    else :
        val = int(tomdat[0].replace('%', ''))
    return val


def get_sorted_recommendations(movies):
    titles = get_related_titles(movies)
    #return titles
    ratings = list(zip([get_movie_rating(get_movie_data(x)) for x in titles], titles))
    #print(ratings)
    ratings=sorted(ratings,key=lambda x: x[0], reverse=True)
    return [x[1] for x in ratings]

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages


movies=["Avengers", "Tron"]
custom=[]
num=int(str(input("Enter Number of Movies:")))
for i in range(num):
    custom.append(input("Enter A Movie :"))
if num!=0:
    movies=custom
else:
    print("Example set")
    print(movies)

print(get_sorted_recommendations(movies))



