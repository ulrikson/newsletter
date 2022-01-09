from messaging.Email import Email
from messaging.Newsletter import Newsletter

newsletter = Newsletter()
content = newsletter.createHTMLMessage()

Email(content).send()
