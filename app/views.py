import requests
from django.shortcuts import render
from django.conf import settings

# TMDB API Configuration
API_KEY = "6a75d08be9b648f1c3c2e60fc26b4818"
BASE_URL = "https://api.themoviedb.org/3"

# Map emotions to movie genres
EMOTION_GENRE_MAP = {
    "select": 3,
    "happy": 35,  # Comedy
    "sad": 18,    # Drama
    "angry": 28,  # Action
    "neutral": 99,  # Documentary
    "surprised": 14,  # Fantasy
    "fear": 27,  # Horror
    "disgust": 80,  # Crime
}

# Fetch movies from TMDB based on genre
def fetch_movies_by_genre(genre_id):
    url = f"{BASE_URL}/discover/movie"
    params = {
        "api_key": API_KEY,
        "with_genres": genre_id,
        "sort_by": "popularity.desc"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("results", [])
    return []
def inp(request):
    
    return render(request, 'index1.html')

def index(request):
    message = ""
    emotion = None
    movies = []

    if request.method == "POST":
        emotion = request.POST.get('emotion')
        if emotion:
            genre_id = EMOTION_GENRE_MAP.get(emotion)  # Default to comedy
            if genre_id == 3:
                message = f"Please Select an EMOTION"
            else:
                movies = fetch_movies_by_genre(genre_id)
                message = f"Showing movie recommendations for the emotion: {emotion.capitalize()}"
                return render(request, 'result.html', {
                    'emotion': emotion,
                    'movies': movies,
                })
    return render(request, 'index1.html',{
        'message': message
    })
