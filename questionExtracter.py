import requests
from bs4 import BeautifulSoup
import os

def extract_company_name(url):
    company_name = url.split(".org/")[1].split("-")[0]
    return company_name.capitalize()

def visit_and_extract_paragraphs(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')

    paragraphs = soup.find_all('p')
    content = "\n".join([p.get_text() for p in paragraphs])

    return content

with open("links.txt", "r") as file:
    links = file.readlines()


for link in links:
    link = link.strip()  

    if link:
        company_name = extract_company_name(link)

        content = visit_and_extract_paragraphs(link)

        filename = f"{company_name}.txt"

        with open(filename, "a") as output_file: 
            output_file.write(content + "\n\n")  
            print(f"Content written to {filename}")
