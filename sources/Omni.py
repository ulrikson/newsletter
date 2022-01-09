from sources.ExternalApi import ExternalApi

import urllib.parse


class Omni(ExternalApi):
    def __init__(self):
        pass

    def getPopularTopics(self):
        url = "https://omni-content.omni.news/topics?offset=0&limit=5&sort=current"
        content = ExternalApi(url).getJson()
        text = self.getTopicsText(content["topics"])

        return text

    def getTopicsText(self, topics):
        topicsList = []

        for topic in topics:
            titleEncoded = urllib.parse.quote(topic["title"])
            url = "https://omni.se/sok?q=" + titleEncoded + "&tab=articles"
            topic = f"<a href={url}>{topic['title']}</a>"
            topicsList.append(topic)

        topicsText = ", ".join(topicsList)

        return topicsText
