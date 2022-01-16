from sources.Covid import Covid
from sources.Omni import Omni
from sources.Weather import Weather

class Newsletter:
    def __init__(self):
        self.covid = Covid().getLatestData()
        self.omni = Omni().getPopularTopics()
        self.weather = Weather("Stockholm", 3).getForecastHtml()

    def createHTMLMessage(self):
        html = f"""\
                <html>
                    <body>
                        <h2>Populärt på Omni</h2>
                        <p>{self.omni}</p>
                        <h2>Dagens covidnytt</h2>
                        <p>{self.covid["critical"]} på IVA, {self.covid["deaths"]} döda och {self.covid["confirmed"]} bekräftade</p>
                        {self.weather}
                    </body>
                </html>
            """

        return html
