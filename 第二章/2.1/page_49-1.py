from urllib import request, error

try:
    response = request.urlopen('https://cuiqingcai.com/404')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')  # 打印错误原因，错误代码，响应头。每个结果之间以换行符分割。
