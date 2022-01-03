from sources.ExternalApi import ExternalApi
import os
from dotenv import load_dotenv
load_dotenv()

class Covid(ExternalApi):
    def __init__(self):
        self.url = "https://covid-19-data.p.rapidapi.com/country"
        self.params = {"name": "sweden"}
        self.headers = {
            "x-rapidapi-host": "covid-19-data.p.rapidapi.com",
            "x-rapidapi-key": os.getenv("RAPID_API_KEY"),
        }
    
    def getLatestData(self):
        content = ExternalApi(self.url, self.headers, self.params).getJson()
        return content[0]
