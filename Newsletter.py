from sources.Covid import Covid


class Newsletter:
    def __init__(self):
        self.covid = Covid().getLatestData()

    def createTextMessage(self):
        text = f"""\
            Tjosvejs!
            
            {self.covid["critical"]} på IVA
            {self.covid["deaths"]} på IVA
            {self.covid["confirmed"]} på IVA
        """

        return text

    def createHTMLMessage(self):
        html = f"""\
                <html>
                    <body>
                        <p>Tjosvejs!</p>
                        <p>{self.covid["critical"]} på IVA</p>
                        <p>{self.covid["deaths"]} döda</p>
                        <p>{self.covid["confirmed"]} bekräftade</p>
                    </body>
                </html>
            """
        
        return html
