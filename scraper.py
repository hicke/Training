import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.nytimes.com/books/best-sellers/')
soup = BeautifulSoup(url.text, 'lxml')

print(soup.title.text)

list = soup.split()
print(list)