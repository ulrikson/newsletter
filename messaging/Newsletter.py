from sources.Covid import Covid


class Newsletter:
    def __init__(self):
        self.covid = Covid().getLatestData()

    def createHTMLMessage(self):
        html = f"""\
                <html>
                    <body>
                        <h2>Dagens covidnytt</h2>
                        <p>{self.covid["critical"]} på IVA, {self.covid["deaths"]} döda och {self.covid["confirmed"]} bekräftade</p>
                    </body>
                </html>
            """

        return html
