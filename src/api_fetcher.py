import requests

def fetch_movie_data(api_key):
    url = "https://api.themoviedb.org/3/movie/popular"
    params = {
        'api_key': api_key,
        'language': 'en-US',
        'page': 1
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data from TMDb:", response.status_code)
        return None

if __name__ == "__main__":
    API_KEY = "3642201f786f1c26bd3ece3fda7a33ce"
    movie_data = fetch_movie_data(API_KEY)
    print(movie_data)
 
