import requests

class FPLApiClient:
    """Client to interact with the Fantasy Premier League API. """
    def __init__(self):
        self.base_url = "https://fantasy.premierleague.com/api/"
        self.session = requests.Session()

    def get(self, endpoint, **kwargs):
        """Send a GET request to the API."""
        url = f"{self.base_url}{endpoint}"
        response = self.session.get(url, **kwargs)
        response.raise_for_status()
        return response.json()