from urllib.parse import urlunsplit

data = ['https', 'www.baidu.com', 'index.html', 'a=6', 'comment']  # 这个参数的长度必须为5，即data无论是什么格式，长度必须为5.
print(urlunsplit(data))
