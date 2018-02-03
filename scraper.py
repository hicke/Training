import requests
import bs4

url = requests.get('http://www.dn.se/')
url.close()
print(url)