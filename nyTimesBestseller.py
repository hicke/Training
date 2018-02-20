import requests
import bs4 as bs
import pprint

url = 'https://www.nytimes.com/books/best-sellers/'
sauce = requests.get(url)
soup = bs.BeautifulSoup(sauce.text, 'lxml')

author = soup.find_all('p', class_='author')
title = soup.find('h3', class_='title')
# print(lists[0:4])
rank = 1
# li = []
for name in author:
    while rank <= 5:
    # pprint.pprint(rank, name.text[3:])
        #print(rank, name.text[2:])
        rank += 1
    # li.append(name.text[2:])
    # print(li)
    # if rank % 5 == 0:
    # print(rank)

cat = soup.find('h2', class_ = 'subcategory-heading')
print(cat.text)