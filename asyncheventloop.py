import asyncio
import requests
import bs4 as bs

def download():
    url_1 = requests.get('https://stackoverflow.com/questions/33357233/when-to-use-and-when-not-to-use-python-3-5-await/33399896#33399896')
    url_2 = requests.get('https://docs.python.org/3/library/asyncio-task.html')
    




async def asyncdownloader(url):
    for a in range(10):
        a_sauce = requests.get(url)
        a_soup = bs.BeautifulSoup(sauce.text, 'lxml')
        print(a)


#downloader('https://www.nytimes.com/books/best-sellers/')
#asyncdownloader('https://www.nytimes.com/books/best-sellers/')

await asyncio.gather(
    download(url_1),
    download(url_2)
)