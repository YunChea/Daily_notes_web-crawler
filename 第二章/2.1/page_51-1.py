from urllib.parse import urlparse

result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
# url中不包含协议时会使用scheme的值
print(result)

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', scheme='https')
# url中包含协议时会使用url自带的协议
print(result)