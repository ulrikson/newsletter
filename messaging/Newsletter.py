from sources.Covid import Covid
from sources.Omni import Omni
from sources.Weather import Weather

class Newsletter:
    def __init__(self):
        self.covid = Covid().getHtml()
        self.omni = Omni().getHtml()
        self.weather = Weather("Stockholm", 3).getHtml()

    def createHTMLMessage(self):
        html = f"""\
                <html>
                    <body>
                        {self.omni}
                        {self.weather}
                        {self.covid}
                    </body>
                </html>
            """

        return html
