# 借助HTTPBasicAuthHandler模块完成基本身份认证(HTTPBasicAccessAuthentication)

from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

username = 'admin'
password = 'admin'
url = 'https://ssr3.scrape.center/'

p = HTTPPasswordMgrWithDefaultRealm()  # 实例化对象HTTPPasswordMgrWithDefaultRealm
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)  # 实例化对象HTTPBasicAuthHandler
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)
