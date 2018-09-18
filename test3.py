import requests
from bs4 import BeautifulSoup
import urllib.request
import re

def get_Image():
    url = 'http://39.107.246.237:8080/htm/'
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    img = soup.findAll('li')
    content = r'<li><img src="(.*?)"/></li>'
    for i in range(len(img)):
        img[i] = str(img[i])
        ans = re.findall(content, img[i], re.S | re.I)
        dizhi = 'http://39.107.246.237:8080/htm/' + ans[0]
        urllib.request.urlretrieve(dizhi, 'E:/chang/'+ str(i) + '.png')

if __name__ == '__main__':
    get_Image()
