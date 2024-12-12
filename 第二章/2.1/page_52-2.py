from urllib.parse import urlunparse  # 注意不再是导入urlparse

data = ['https', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))
