import requests

def get_todays_random_quote():
    results = requests.get("https://dummyjson.com/quotes/random")
    results_json = results.json()
    return results_json