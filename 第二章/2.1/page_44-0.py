import urllib.request

request = urllib.request.Request('https://python.org')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))

"""
urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
url为URL，必须参数。
data为要传输的数据，类型为bytes。
headers为请求头。
origin_req_host为请求方（即发起请求的一方，用于标注请求来源于哪里。）的host名称或者IP地址。
如果不确定本地主机名，可以用以下代码获取：
    -------------------------
    import socket
    
    local_hostname = socket.gethostname()
    print(local_hostname)
    -------------------------
unverifiable为是否是无法验证的。
method为指示请求的方法，方法为GET，POST等（见第一章/第一章笔记.md）（通常必须是大写）
"""
