import json
import bs4 as bs
import requests
import json

def js():
    url = 'https://picsum.photos/list'
    sauce = requests.get(url)
    soup = bs.BeautifulSoup(sauce.text,'lxml')
    json_string = json.dumps(soup.text)
    data = json.loads(json_string)
    return data["author"]
js()