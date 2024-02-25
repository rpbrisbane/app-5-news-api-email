import requests

api_key = "8b871d740c3c45a8b45c16fc904bc346"
url = ("https://newsapi.org/v2/everything?q=tesla&"
       "from=2024-01-25&sortBy=publishedAt&apiKey="
       "8b871d740c3c45a8b45c16fc904bc346")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
