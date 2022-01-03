import requests


class Scraper:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def getContent(self):
        response = requests.get(self.url, self.headers)
        return response.content
