from sources.ExternalApi import ExternalApi
import os
from dotenv import load_dotenv

load_dotenv()


class Weather(ExternalApi):
    def __init__(self, city, days):
        self.url = "http://api.weatherapi.com/v1/forecast.json"
        self.city = city
        self.days = days
        self.params = {
            "key": os.getenv("WEATHER_API_KEY"),
            "q": self.city,
            "days": self.days,
        }
        self.headers = {}

    def getHtml(self):
        forecasts = self.getForecast()

        html = "<h2>Väder</h2>"

        for day in forecasts:
            text = f"<p>{day['date']}: {day['text']}, {day['avg_temp']} grader och {day['precipitation']} mm nederbörd"
            html = html + text

        smhiUrl = f"https://www.smhi.se/q/{self.city}"
        link = f"<p><a url={smhiUrl}>Mer info</p></a>"

        html = html + link

        return html

    def getForecast(self):
        content = ExternalApi(self.url, self.headers, self.params).getJson()

        forecasts = []

        for forecast in content["forecast"]["forecastday"]:
            date = forecast["date"]
            avgTemp = forecast["day"]["avgtemp_c"]
            totalPrecipitation = forecast["day"]["totalprecip_mm"]
            condition = forecast["day"]["condition"]["text"]

            forecasts.append(
                {"date": date, "avg_temp": avgTemp, "precipitation": totalPrecipitation, "text": condition}
            )

        return forecasts
