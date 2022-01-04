from Email import Email
from Newsletter import Newsletter

newsletter = Newsletter()
text = newsletter.createTextMessage()
html = newsletter.createHTMLMessage()

Email(text, html).sendEmail()
