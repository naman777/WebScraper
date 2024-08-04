import requests
from bs4 import BeautifulSoup

url = "https://www.geeksforgeeks.org/experienced-interview-experiences-company-wise/"

response = requests.get(url)
with open("sample.html","w") as f:
    f.write(response.text)


with open("sample.html","r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')

links = soup.find_all("a")

with open("links.txt", "w") as f:
    for link in links:
        href = link.get("href")
        if href and "interview" in href:
            f.write(href + "\n")

