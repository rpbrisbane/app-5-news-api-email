import requests
from send_email import send_email

api_key = "8b871d740c3c45a8b45c16fc904bc346"
url = ("https://newsapi.org/v2/everything?q=tesla&"
       "from=2024-01-25&sortBy=publishedAt&apiKey="
       "8b871d740c3c45a8b45c16fc904bc346")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
message = ""
for article in content["articles"]:
    title = article["title"]
    description = article["description"]
    if title and description is not None:
        message = message + title + "\n" + description + "\n" + "\n"

message = message.encode("utf-8")
send_email(message=message)




