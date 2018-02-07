import requests
import bs4 as bs
import redis

r = redis.StrictRedis(host='localhost', port=32768, db=3)
url = 'https://httpstatuses.com/'
sauce = requests.get(url)
soup = bs.BeautifulSoup(sauce.text,'lxml')
#print(soup.prettify)

all_lists = soup.find_all('li')
i = []

def http_to_redis():
    for li in all_lists:
        i.append(li.text)
           
        for num in i:
            error = num.split()
            error_code = error[0]
            error_text = ' '.join(map(str, error[1:]))
            r.set(error_code, error_text, 100)
            #print(error_code, error_text

http_to_redis()