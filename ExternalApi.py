import requests


class ExternalApi:
    def __init__(self, url, headers, params):
        self.url = url
        self.headers = headers
        self.params = params

    def getJson(self):
        response = requests.get(self.url, headers=self.headers, params=self.params)
        return response.json()
