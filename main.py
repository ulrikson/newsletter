from messaging.Email import Email
from messaging.Newsletter import Newsletter

newsletter = Newsletter()
content = newsletter.createHTMLMessage()

# print(content)
# Email(content).sendViaMailtrap()
Email(content).send()
