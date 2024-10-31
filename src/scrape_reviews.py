import requests
from bs4 import BeautifulSoup

def scrape_reviews(movie_id):
    """
    Scrape reviews for a specific movie from a review site.
    Parameters:
        movie_id (int): The ID of the movie to scrape reviews for.
    Returns:
        reviews (list): List of scraped reviews.
    """
    url = f"https://www.example.com/movies/{movie_id}/reviews"  # Replace with the actual URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    reviews = []
    for review in soup.find_all('div', class_='review'):  # Update based on the actual HTML structure
        reviews.append(review.get_text(strip=True))

    return reviews

if __name__ == "__main__":
    movie_id = 1  # Example movie ID
    reviews = scrape_reviews(movie_id)
    print("Scraped Reviews:", reviews)
 
