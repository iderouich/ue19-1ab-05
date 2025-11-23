import requests

API_URL = "https://api.chucknorris.io/jokes/random"


def get_random_joke():
    """Récupère une blague aléatoire via l'API publique."""
    response = requests.get(API_URL, timeout=5)
    response.raise_for_status()  # lève une erreur si la requête a échoué
    data = response.json()
    return data.get("value", "Impossible de récupérer une blague.")


def main():
    print("=== Chuck Norris Joke ===")
    try:
        joke = get_random_joke()
        print(joke)
    except requests.RequestException as e:
        print("Erreur lors de l'appel à l'API :", e)


if __name__ == "__main__":
    main()
