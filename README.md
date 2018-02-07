# Python training

#### API
* Flask
* API Gateway
---
#### Databases
* DynamoDB
* MangoDB
* Redis
---
#### AWS
---
#### Threading
* Threading module
* Asyncio(?)
---
#### Web scraping

#### *Tools used*
* BeautifulSoap
    * Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    * Example:
```python
    import requests
    from bs4 import BeautifulSoup

    url = requests.get('https://www.nytimes.com/')
    soup = BeautifulSoup(url.text, 'lxml')

    print(soup.title.text)
```
#### Encrypt/Decrypt (jwe, jws)
