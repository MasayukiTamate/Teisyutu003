from bs4 import BeautifulSoup
import requests

url = "https://toukei-lab.com/scraping_training"

response = requests.get(url, timeout=100)
soup = BeautifulSoup(response.text, "html.parser")


for tag in soup.select("#toc_container > p"):
    print(tag.get_text())

for tag in soup.select("#main-contents > section > article > div.cps-post-main-box > div > p:nth-child(4)"):
    print(tag.get_text())