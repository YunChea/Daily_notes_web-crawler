import urllib.request
import urllib.parse

# 如果报错，检查'utf-8'及'https://www.httpbin.org/post'是否有拼写错误。
data = bytes(urllib.parse.urlencode({'name': 'germey'}), encoding='utf-8')
response = urllib.request.urlopen('https://www.httpbin.org/post', data=data)
print(response.read().decode('utf-8'))

'''输出内容:
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
    "User-Agent": "Python-urllib/3.9", 
    "X-Amzn-Trace-Id": "Root=1-6756dbde-2117d2441acf783e0ce4099e"
  }, 
  "json": null, 
  "origin": "125.42.99.79", 
  "url": "https://www.httpbin.org/post"
}
'''