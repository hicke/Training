import bs4 as bs
import requests

book_url = requests.get("https://www.nytimes.com/books/best-sellers/")
sauce = bs.BeautifulSoup(book_url.text, 'lxml')
print(sauce)