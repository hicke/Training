import bs4
import requests

book_url = requests.get("https://www.nytimes.com/books/best-sellers/").text
print(book_url)