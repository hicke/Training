import requests
import bs4 as bs
import redis

r = redis.StrictRedis(host='localhost', port=32768, db=3)
url = 'https://httpstatuses.com/'
sauce = requests.get(url)
soup = bs.BeautifulSoup(sauce.text, 'lxml')
# print(soup.prettify)

all_lists = soup.find_all('li')
i = []

for li in all_lists:
    i.append(li.text)

    for num in i:
        error = num.split()
        error_code = error[0]
        error_text = ' '.join(map(str, error[1:]))
        # r.set(error_code, error_text, 100)
        # print(url + error_code)


full_url = url + error_code
f = requests.get(full_url)
# print(f.text)


def get_full_text():

    new_sauce = requests.get(full_url)
    new_soup = bs.BeautifulSoup(new_sauce.text, 'lxml')
    for paragraph in new_soup:
        print(new_soup.p)
