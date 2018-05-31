# Http 请求的 Python 实现
# urllib2 和 urllib 是 Python 中的两个内置模块, 要实现 HTTP 功能,
# 实现方式以 urllib2 为主, urllib 为辅.
# 1. 首先实现一个完整的请求与响应模型
# urllib2 提供一个基础函数 urlopen, 通过向指定的 URL 发送请求来获取
# 数据.

import urllib.parse
import urllib.request
import http.cookiejar

# GET 请求
# response = urllib.request.urlopen('http://www.zhihu.com')
# html = response.read()
# print(html)

# POST 请求
# url = 'http://www.xxxxxx.com/login'
# postdata = {'username': 'qiye', 'password': 'qiye_pass'}
# data = urllib.parse.urlencode(postdata).encode('utf-8')
# req = urllib.request.Request(url, data)
# response = urllib.request.urlopen(req)
# html2 = response.read()

# 请求头 Headers 处理
# url = 'http://www.xxxxxx.com/login'
# user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
#              'Chrome/66.0.3359.181 Safari/537.36'
# referer = 'http://www.xxxxxx.com/'
# postdata = {'username': 'qiye', 'password': 'qiye_pass'}
# # 将 user_agent, referer 写入头信息
# headers = {'User-Agent': user_agent, 'Referer': referer}
# data = urllib.parse.urlencode(postdata).encode('utf-8')
# req = urllib.request.Request(url, data, headers)
# response = urllib.request.urlopen(req)
# html3 = response.read()
# req 的创建方式也可以改写为以下方式
# req = urllib.request.Request(url, data)
# req.add_header('User-Agent', user_agent)
# req.add_header('Referer', referer)

# Cookie 处理
# cookie = http.cookiejar.CookieJar()
# opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
# response = opener.open('https://www.baidu.com')
# for item in cookie:
#     print(item.name + ':' + item.value)

# 但是有时候会遇到这种情况, 我们不想让 urllib 自动处理, 我们想自己添加 Cookie 的
# 内容, 可以通过设置请求头中的 Cookie 域来做:
# opener = urllib.request.build_opener()
# opener.addheaders.append(('Cookie', 'email=xxxxxx@163.com'))
# req = urllib.request.Request('https://www.baidu.com/')
# response = opener.open(req)
# print(response.headers)
# retdata = response.read()

# Timeout 设置超时
# request = urllib.request.Request('https://www.baidu.com')
# response = urllib.request.urlopen(request, timeout=2)
# html = response.read()
# print(html)

# 获取 HTTP 响应码
# 对于 200 OK 来说, 只要使用 urlopen 返回的 response 对象的 getcode() 方法
# 就可以得到 HTTP 的返回码. 但对其他返回码来说, urlopen 会抛出异常. 这时候, 就要检查
# 异常对象的 code 属性了, 示例代码如下:
# try:
#     response = urllib.request.urlopen('https://www.google.com')
#     print(response)
# except urllib.request.HTTPError as e:
#     if hasattr(e, 'code'):
#         print('Error code:', e.code)

# 重定向
# urllib 默认情况下会针对 HTTP 3XX 返回码自动进行重定向动作. 要检测是否发生了
# 重定向动作, 只要检查一下 Request 的 URL 和 Request 的 URL 是否一致就可以了,
# 示例代码如下:
# response = urllib.request.urlopen('https://www.baidu.com')
# isRedirected = response.geturl() == 'https://www.baidu.com'
# print(isRedirected)
# 如果不想自动重定向, 可以自定义 HTTPRedirectHandler 类, 示例代码如下:
# class RedirectHandler(urllib.request.HTTPRedirectHandler):
#     def http_error_301(self, req, fp, code, msg, headers):
#         pass
#     def http_error_302(self, req, fp, code, msg, headers):
#         result = urllib.request.HTTPRedirectHandler.http_error_301(self, req, fp, code, msg, headers)
#         result.status = code
#         result.newurl = result.geturl()
#         return result
# opener = urllib.request.build_opener(RedirectHandler)
# opener.open('http://www.zhihu.cn')

# Proxy 的设置
# 在做爬虫开发中, 必不可少地会用到代理. urllib 默认会使用环境变量 http_proxy 来设置
# HTTP Proxy. 但是我们一般不采用这种方式, 而是使用 ProxyHandle 在程序中动态设置代理,
# 示例代码如下:
# proxy = urllib.request.ProxyHandler({'http': '127.0.0.1:8087'})
# opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
# urllib.request.install_opener(opener)
# response = urllib.request.urlopen('https://www.baidu.com/')
# print(response.read())
# 这里要注意的一个细节, 使用 urllib.request.install_opener() 会设置 urllib 的全局 opener,
# 之后所有的 HTTP 访问都会使用这个代理. 这样使用会很方便, 但不能做更细粒度的控制, 比如
# 想在程序中使用两个不同的 Proxy 设置, 这种场景在爬虫中很常见. 比较好的做法是不使用 install_opener
# 去更改全局的设置, 而只是直接调用 opener 的 open 方法代替全局的 urlopen 方法, 修改如下:
proxy = urllib.request.ProxyHandler({'http': '127.0.0.1:8087'})
opener = urllib.request.build_opener(proxy)
response = opener.open('https://www.baidu.com/')
print(response.read())