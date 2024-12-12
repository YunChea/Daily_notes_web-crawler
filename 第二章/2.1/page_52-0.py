from urllib.parse import urlparse

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
print(result)

result_2 = urlparse('http://www.baidu.com/index.html#comment', allow_fragments=False)
print(result_2)