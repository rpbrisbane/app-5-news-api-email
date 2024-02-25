import requests
from send_email import send_email

topic = "tesla"
api_key = "8b871d740c3c45a8b45c16fc904bc346"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "from=2024-01-25&"
       "sortBy=publishedAt&"
       "apiKey=8b871d740c3c45a8b45c16fc904bc346&"
       "language=en")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
message = ""
for article in content["articles"][:20]:
    title = article["title"]
    description = article["description"]
    article_url = article["url"]
    if title and description is not None:
        message = ("Subject: Today's news: " + "\n"
                   + message + title + "\n"
                   + description + "\n"
                   + article_url + 2*"\n")

message = message.encode("utf-8")
send_email(message=message)




