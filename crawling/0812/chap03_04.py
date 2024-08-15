from urllib.parse import urlparse

urlstring1='https://shopping.naver.com/home/p/index.naver'

url=urlparse(urlstring1)
print(url.scheme)
print(url.netloc)
print(url.path)