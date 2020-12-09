import requests


class ApiConnectionClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.api_key = 'edbad9163788957'

    def post(self, route: str, body: dict, file=None, headers=None):
        headers = {'apikey': self.api_key}
        route = self.base_url + route
        response = requests.post(url=route, data=body, files=file, headers=headers)
        return response.json()

