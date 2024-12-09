import urllib.request

response = urllib.request.urlopen('https://www.python.org')  # 同30-0
print(response.status)  # 打印出响应的状态码
print(response.getheaders())  # 打印出响应的头信息
print(response.getheader('Server'))  # 打印响应头中的Server值，2024.12.9执行此代码时响应中没有server（可能是隐藏了）。
