import requests
from bs4 import BeautifulSoup

username = input("Enter username:")
URL = 'https://www.instagram.com/{}/'

response = requests.get(URL.format(username))
s = BeautifulSoup(response.text, "html.parser")
u = s.find("meta", property="og:image")
url = u.attrs["content"]

with open(username + ".jpg", "wb") as pic:
    binary = requests.get(url).content
    pic.write(binary)
