import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = os.getenv("API_KEY")


def fetch_data (animal_name):
    """Gets the animals data from amnimals api."""
    if not API_KEY:
        print("Error: API Key is missing. Please check your .env file.")
        return []

    response = requests.get(
        API_URL,
        headers={"X-Api-Key": API_KEY},
        params={"name": animal_name}
    )

    if response.status_code == 200:
        data = response.json()
        if data:
            return data
        else:
            print("Sorry, no animals found for you.")
            return []
    else:
        print(f"Error: {response.status_code}")
        return []
