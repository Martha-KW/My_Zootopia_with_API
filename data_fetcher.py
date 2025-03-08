import requests

API_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = "2TZVJsSaOT2TrVN9mItbaA==c1g3aSnr36B79P9Q"

def fetch_data (animal_name):
    """Gets the animals data from amnimals api."""
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
