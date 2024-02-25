import streamlit as st
import requests


api_key = "qTsqjgpdWP9aeC1qq0sELuNy802Y27ryko1J0yCR"
url = ("https://apod.nasa.gov/apod?"
       f"api_key={api_key}")


request = requests.get(url)

content = request.json()

title = content["title"]
title = title.encode("utf-8")
image_url = content["url"]
explanation = content["explanation"]
explanation = explanation.encode("utf-8")

st.title(title)
st.image(image_url)
st.write(explanation)

