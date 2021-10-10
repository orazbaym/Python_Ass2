import requests
from bs4 import BeautifulSoup

url = "https://api.coinmarketcap.com/content/v3/news?coins=4030&page=1&size=5"

data = {
    'coins': '4030',
    'page': '1',
    'size': '5',
    }

Headers = {
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'origin': 'https://coinmarketcap.com',
    'referer': 'https://coinmarketcap.com/',
    'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    }
    
def returnJsonRequest(url):
    r = requests.get(url,headers = Headers,params = data)
    return r.json()

def returnTitle(json):
    a = []
    for i in json['data']:
        a.append(i['meta']['title'])
    return a

def returnDesc(json):
    a = []
    for i in json['data']:
        a.append(i['meta']['subtitle'])
    return a

def printPage(a,b):
    for i in range(len(a)):
        print("\033[1m" , a[i] , "\033[0m",'\n')
        print("\t", b[i],'\n')
        print(".......................................................................", '\n')
    pass

printPage(returnTitle(returnJsonRequest(url)),returnDesc(returnJsonRequest(url)))