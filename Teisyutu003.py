from bs4 import BeautifulSoup
import requests

url = "https://www.amazon.co.jp/?tag=lenovo01-22&linkCode=ure&creative=6339"

response = requests.get(url, timeout=100)
soup = BeautifulSoup(response.text, "html.parser")

print(response.text)
print("タイトル",soup.titel)
print(soup.string)