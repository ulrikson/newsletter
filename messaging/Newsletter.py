from sources.Covid import Covid
from sources.Omni import Omni
from sources.Weather import Weather
from sources.TV import TV

class Newsletter:
    def __init__(self):
        self.covid = Covid().getHtml()
        self.omni = Omni().getHtml()
        self.weather = Weather("Stockholm", 3).getHtml()
        self.tv = TV().getHtml()

    def createHTMLMessage(self):
        html = f"""\
                <html>
                    <body>
                        {self.omni}
                        {self.weather}
                        {self.covid}
                        {self.tv}
                    </body>
                </html>
            """

        return html
