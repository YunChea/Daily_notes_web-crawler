import urllib.request, http.cookiejar

cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookie_LWP.txt', ignore_discard=True, ignore_expires=True)  # 读取文件内容（读取的时LWP格式的）
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
print(response.read().decode('utf-8'))
