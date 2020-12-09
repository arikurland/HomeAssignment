import requests


class ApiConnectionClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.api_key = 'edbad9163788957'

    def post(self, url, body, file=None, headers=None):
        headers = {'apikey': self.api_key}
        url = self.base_url + url
        response = requests.post(url=url, data=body, files=file, headers=headers)
        return response.json()

