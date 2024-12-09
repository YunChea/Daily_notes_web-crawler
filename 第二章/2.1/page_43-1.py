import socket
import urllib.request
import urllib.error

try:  # 尝试执行try内的内容，若失败则执行except中的内容。
    response = urllib.request.urlopen('https://www.httpbin.org/get', timeout=0.1)  # 0.1的单位为秒，python中的时间单位一般为秒。
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):  # 使用 isinstance(e.reason, socket.timeout) 检查异常的具体原因是否为 socket.timeout。如果是，则打印 'TIME OUT'。
        print('TIME OUT')
# try中的内容如果执行时报错，则会执行except中的内容，
# 这里写urllib.error.URLError as e的原因是要获取捕获的的异常对象，如果直接打印urllib.error.URLError则是打印这个类本身，内容为“<class 'urllib.error.URLError'>”
# 而打印e则内容为“<urlopen error timed out>”，e的类型为“<class 'urllib.error.URLError'>”

""" 输出内容：
TIME OUT

进程已结束，退出代码为 0
"""