from .fpl_api_client import FPLApiClient

class BootstrapAPI:
    """A class to handle API requests with bootstrap-static data functionality."""
    def __init__(self, api_client: FPLApiClient):
        self.api_client = api_client
        self.bootstrap_data = None

    def fetch_bootstrap_data(self):
        """Fetch the bootstrap-static data from the API."""
        if self.bootstrap_data is None:
            self.bootstrap_data = self.api_client.get("bootstrap-static/")
        return self.bootstrap_data
    
    def get_players(self):
        """Get the list of players from the bootstrap data."""
        data = self.fetch_bootstrap_data()
        return data.get("elements", [])
    
    def get_teams(self):
        """Get the list of teams from the bootstrap data."""
        data = self.fetch_bootstrap_data()
        return data.get("teams", [])
    
    def get_gameweeks(self):
        """Get the list of gameweeks from the bootstrap data."""
        data = self.fetch_bootstrap_data()
        return data.get("events", [])

    def get_positions(self):
        """Get the list of player positions from the bootstrap data."""
        data = self.fetch_bootstrap_data()
        return data.get("element_types", [])