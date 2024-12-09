from urllib import request, parse

url = 'https://www.httpbin.org/post'  # 请求的地址
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',  # 请求头的UA/用户代理，User-Agent 是一个标头字段，用于标识发出请求的客户端应用程序、操作系统、供应商和版本信息。它通常由浏览器、爬虫或其他 HTTP 客户端库自动设置。
    'Host': 'www.httpbin.org'  # 同之前
}# 指定UA和Host
dict = {'name': 'germey'}
data = bytes(parse.urlencode(dict), encoding='utf-8')  # 将字典数据转换为字节流格式，编码类型为utd-8
req = request.Request(url=url, data=data, headers=headers, method="POST")
response = request.urlopen(req)  # 同之前
print(response.read().decode('utf-8'))  # 同之前



""" 完整输出内容：
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "name": "germey"
  }, 
  "headers": {
    "Accept-Encoding": "identity", 
    "Content-Length": "11", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "www.httpbin.org", 
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)", 
    "X-Amzn-Trace-Id": "Root=1-6756e918-1325f8ce12c44d17135faea3"
  }, 
  "json": null, 
  "origin": "125.42.99.79", 
  "url": "https://www.httpbin.org/post"
}


进程已结束，退出代码为 0

"""