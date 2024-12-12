from urllib import request, error

try:
    response = request.urlopen('https://cuiqingcai.com/404')
except error.HTTPError as e:  # 如果返回HTTP Error错误，那么打印错误原因，状态码，响应头信息（书上这里写的是请求头，个人觉得应该是写错了。）
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('Request Successfully')
