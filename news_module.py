import requests
import random
from stt import speak

API_KEY = "5484f80f87ac48488487687b0309e432"
BASE_URL = "https://newsapi.org/v2/top-headlines"
COUNTRY = "in"

def get_news(category=None, count=5):
    try:
        params = {
            "country": COUNTRY,
            "apiKey": API_KEY
        }
        if category:
            params["category"] = category.lower()

        response = requests.get(BASE_URL, params=params)
        data = response.json()

        # Debugging: Print raw response if status not OK
        if data.get("status") != "ok" or not data.get("articles"):
            print("Full API Response for Debugging:\n", data)
            raise Exception("No news data available.")

        articles = data["articles"]
        random.shuffle(articles)

        selected = articles[:count]
        headlines = [article["title"] for article in selected]

        headline_text = f"Today's top {category or 'general'} headlines:\n" + "\n".join(headlines)
        print(headline_text)
        return headline_text

    except Exception as e:
        error_msg = f"Error fetching news: {e}"
        print(error_msg)
        return error_msg

# Example usage
news_text = get_news(category="tech")

speak(news_text)
