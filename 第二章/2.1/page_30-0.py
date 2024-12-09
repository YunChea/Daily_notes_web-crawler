import urllib.request

response = urllib.request.urlopen('https://www.python.org')
# 调用urllib.request模块中的函数urlopen打开地址‘https://www.python.org’，这将返回一个HTTPResponse对象（类型(type())为'http.client.HTTPResponse'），将给对象赋给response
print(response.read().decode('utf-8'))
# 调用HTTPResponse对象（即response）的方法read()读取其中的数据，读取的数据会以字节串的形式返回，然后再使用decode()方法按照utf-8编码将字节串转换为人类可读的字符串。

