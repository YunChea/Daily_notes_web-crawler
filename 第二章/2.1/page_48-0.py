import urllib.request, http.cookiejar

filename = 'cookie.txt'
filename_2 = 'cookie_LWP.txt'

# 默认保存格式
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)
"""
    ignore_discard参数类型为bool，如果设置为True，则保存cookies时会忽略被标记为"discard"的cookies，
    这些cookies通常是用户明确选择不保存的（例如通过浏览器设置的）。
    discard是cookie的一个属性，标记用于指示浏览器是否应该丢弃该cookie，当一个cookie被标记为discard时，
    该cookie不会保存到磁盘上，这意味着用户关闭并重新打开浏览器，该cookie不会被留。
    常用于用户隐私（关闭浏览器后不会保留任何会话信息）或者临时数据（仅在会话中使用一次，不需要长期存储）。
    
    ignore_expores参数类型为bool，如果设置为True，则在保存cookies时会忽略那些已经过期的cookies。
    即使这些cookies已经过期，它们仍然会被保留下来。（因为默认情况下是不会保留已过期的cookies的，该参数
    为True时会忽略是否过期这一属性。）
"""

# LWP保存格式
cookie_2 = http.cookiejar.LWPCookieJar(filename_2)
handler_2 = urllib.request.HTTPCookieProcessor(cookie_2)
opener_2 = urllib.request.build_opener(handler_2)
response_2 = opener_2.open('https://www.baidu.com')
cookie_2.save(ignore_discard=True, ignore_expires=True)
