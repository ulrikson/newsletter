from sources.ExternalApi import ExternalApi
import os
from dotenv import load_dotenv
load_dotenv()

url = "https://covid-19-data.p.rapidapi.com/country"
params = {"name": "sweden"}
headers = {
    "x-rapidapi-host": "covid-19-data.p.rapidapi.com",
    "x-rapidapi-key": os.getenv("RAPID_API_KEY"),
}

content = ExternalApi(url, headers, params).getJson()

print(content)