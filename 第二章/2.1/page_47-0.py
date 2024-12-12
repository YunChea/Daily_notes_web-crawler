from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy_handler = ProxyHandler({
    'http': 'http://127.0.0.1:8080',
    'https:': 'https://127.0.1:8080'
})  # 设置代理
opener = build_opener(proxy_handler)  # 构建一个有代理的opener对象
try:
    response = opener.open('https://www.baidu.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
