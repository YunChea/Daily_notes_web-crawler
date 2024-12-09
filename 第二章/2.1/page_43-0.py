import urllib.request

response = urllib.request.urlopen('https://www.httpbin.org', timeout=0.1)
print(response.read())

""" 完整报错:
Traceback (most recent call last):
  File "C:\Users\19141\AppData\Local\Programs\Python\Python39\lib\urllib\request.py", line 1346, in do_open
    h.request(req.get_method(), req.selector, req.data, headers,
  File "C:\Users\19141\AppData\Local\Programs\Python\Python39\lib\http\client.py", line 1255, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\19141\AppData\Local\Programs\Python\Python39\lib\http\client.py", line 1301, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\19141\AppData\Local\Programs\Python\Python39\lib\http\client.py", line 1250, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\19141\AppData\Local\Programs\Python\Python39\lib\http\client.py", line 1010, in _send_output
    self.send(msg)
  File "C:\Users\19141\AppData\Local\Programs\Python\Python39\lib\http\client.py", line 950, in send
    self.connect()
  File "C:\Users\19141\AppData\Local\Programs\Python\Python39\lib\http\client.py", line 1417, in connect
    super().connect()
  File "C:\Users\19141\AppData\Local\Programs\Python\Python39\lib\http\client.py", line 921, in connect
    self.sock = self._create_connection(
  File "C:\Users\19141\AppData\Local\Programs\Python\Python39\lib\socket.py", line 843, in create_connection
    raise err
  File "C:\Users\19141\AppData\Local\Programs\Python\Python39\lib\socket.py", line 831, in create_connection
    sock.connect(sa)
socket.timeout: timed out

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:\pycharm\Python3网络爬虫开发实战-第2版-(崔庆才)\第二章\2.1\page_43-0.py", line 3, in <module>
    response = urllib.request.urlopen('https://www.httpbin.org', timeout=0.1)
  File "C:\Users\19141\AppData\Local\Programs\Python\Python39\lib\urllib\request.py", line 214, in urlopen
    return opener.open(url, data, timeout)
  File "C:\Users\19141\AppData\Local\Programs\Python\Python39\lib\urllib\request.py", line 517, in open
    response = self._open(req, data)
  File "C:\Users\19141\AppData\Local\Programs\Python\Python39\lib\urllib\request.py", line 534, in _open
    result = self._call_chain(self.handle_open, protocol, protocol +
  File "C:\Users\19141\AppData\Local\Programs\Python\Python39\lib\urllib\request.py", line 494, in _call_chain
    result = func(*args)
  File "C:\Users\19141\AppData\Local\Programs\Python\Python39\lib\urllib\request.py", line 1389, in https_open
    return self.do_open(http.client.HTTPSConnection, req,
  File "C:\Users\19141\AppData\Local\Programs\Python\Python39\lib\urllib\request.py", line 1349, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error timed out>

进程已结束，退出代码为 1

"""
