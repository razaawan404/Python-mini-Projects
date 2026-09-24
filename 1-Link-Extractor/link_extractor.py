import requests
import urllib


url = "https://books.toscrape.com/"

response = requests.get(url)

print(response.text)