# 获取网站cookie

import http.cookiejar
import urllib.request

cookie = http.cookiejar.CookieJar()  # 声明CookieJar对象
handler = urllib.request.HTTPCookieProcessor(cookie)  # 构建Handler
opener = urllib.request.build_opener(handler)  # 构建opener
response = opener.open('https://www.baidu.com')
for item in cookie:
    print(item.name + '=' + item.value)

"""输出结果：
BAIDUID=06E3C2B7901D434496C5F0D2D432B882:FG=1
BIDUPSID=06E3C2B7901D43449C2EC77F39EA63F5
PSTM=1734002603
BD_NOT_HTTPS=1

进程已结束，退出代码为 0

"""