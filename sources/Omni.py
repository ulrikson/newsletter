from ExternalApi import ExternalApi

import json


class Omni(ExternalApi):
    def __init__(self):
        pass

    def getPopularTopics(self):
        url = "https://omni-content.omni.news/topics?offset=0&limit=5&sort=current"
        content = ExternalApi(url).getJson()
        topics = content["topics"]

        topicsList = [topic["title"] for topic in topics]
        topicsText = ", ".join(topicsList)

        return topicsText

print(
    Omni().getPopularTopics()
)
