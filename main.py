from Email import Email
from Newsletter import Newsletter

newsletter = Newsletter()
content = newsletter.createHTMLMessage()

Email(content).sendViaMailtrap()
