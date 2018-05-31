# 更人性化的 Requests
# Python 中 Requests 实现 HTTP 请求的方式, 是本人极力推荐的, 也是在 Python 爬虫开发
# 中最为常用的方式. Requests 实现 HTTP 请求非常简单, 操作更人性化.
# Requests 库是第三方模块, 需要额外进行安装. Requests 是一个开源库, 源码位于
# Github:https://github.com/kennethreitz/requests, 希望大家多多支持作者.
# 使用 Requests 库需要先进行安装, 一般有两种安装方式:
# 1) 使用 pip 进行安装, 安装命令为: pip install requests, 不过可能不是最新版.
# 2) 直接到 Github 上下载 Requests 的源代码, 下载链接为: https://github.com/kennethreitz/requests/releases.
# 将源代码压缩包进行解压, 然后进入解压后的文件夹, 运行 setuo.py 文件即可.

import requests

# GRT 请求
# req = requests.get('http://www.baidu.com')
# print(req.content)

# POST 请求
# postdata = {'key': 'value'}
# req = requests.post('http://www.xxxxxx.com/login', data=postdata)
# print(req.content)

# HTTP 中的其他请求方式也可以用 Requests 来实现, 示例如下:
# r = requests.put('http://www.baidu.com/put', data={'key': 'value'})
# r = requests.delete('http://www.baidu.com/delete')
# r = requests.head('http://www.baidu.com/get')
# r = requests.options('http://www.baidu.com/get')

# 接着讲解一下稍微复杂的方式, 大家肯定见过类似这样的
# URL:http://zzk.cnblogs.com/s/blogpost?Keywords=blog:qiyeboy&pageindex=1,
# 也就是在网址后面紧跟着'?', '?'后面还有参数. 那么这样的 GET 请求该如何发送呢?
# 肯定有人会说, 直接将完整的 URL 带入即可, 不过 Requests 还提供了其他方式, 示例如下:
# payload = {'Keywords': 'blog:qiyeboy', 'pageindex': 1}
# r = requests.get('http://zzk.cnblogs.com/s/blogpost', params=payload)
# print(r.url)

# 响应与编码
# r = requests.get('http://www.baidu.com')
# print('content-->%s' % r.content)
# print('text-->%s' % r.text)
# print('encoding-->%s' % r.encoding)
# r.encoding = 'utf-8'
# print('new text-->%s' % r.text)

# chardet, 这是一个非常优秀的字符串/文件编码检测模块.

import chardet

# r = requests.get('http://www.baidu.com')
# print(chardet.detect(r.content))
# r.encoding = chardet.detect(r.content)['encoding']
# print(r.text)

# 直接将 chardet 探测到的编码, 赋给 r.encoding 实现解码, r.text 输出就不会有乱码了.
# 除了上面那种直接获取全部响应的方式, 还有一种流模式, 示例如下:
# r = requests.get('http://www.baidu.com', stream=True)
# print(r.raw.read(10))
# 设置 stream=True 标志位, 使响应以字节流方式进行读取, r.raw.read 函数指定读取的字节数.

# 请求头 headers 处理
# Requests 对 headers 的处理和 urllib 非常相似, 在 Requests 的 get 函数中添加 headers 参数
# 即可, 示例如下:
# user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
#              'Chrome/66.0.3359.181 Safari/537.36'
# headers = {'User-Agent': user_agent}
# r = requests.get('https://www.baidu.com', headers=headers)
# print(r.content)

# 响应码 code 和响应头 headers 处理
# 获取响应码是使用 Requests 中的 status_code 字段, 获取响应头使用 Requests 中的 headers
# 字段. 示例如下:

# r = requests.get('https://www.baidu.com')
# if r.status_code == requests.codes.ok:
#     print(r.status_code) # 响应码
#     print(r.headers) # 响应头
#     print(r.headers.get('content-type')) # 推荐使用这种获取方式, 获取其中的某个字段
#     print(r.headers['content-type']) # 不推荐使用这种获取方式
# else:
#     r.raise_for_status()

# 上述程序中, r.headers 包含所有的响应头信息, 可以通过 get 函数获取自重的某一个字段,
# 也可以通过字典引用的方式获取字典值, 但是不推荐, 因为如果字段中没有这个字段, 第二种
# 方式会抛出异常, 第一种方式会返回 None. r.raise_for_status() 是用来主动地产生一个
# 异常, 当响应码是 4XX 或 5XX 时, raise_for_status() 函数会抛出异常, 而响应码为200时,
# raise_for_status() 函数返回 None.

# Cookie 处理
# 如果响应中包含 Cookie 的值, 可以如下方式湖区 Cookie 字段的值, 示例如下:

# user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
#              'Chrome/66.0.3359.181 Safari/537.36'
# headers = {'User-Agent': user_agent}
# cookies = dict(name='qiye', age='10')
# r = requests.get('https://www.baidu.com', headers=headers, cookies=cookies)
# r.encoding = chardet.detect(r.content)['encoding']
# print(r.text)

#  还有一种更加高级的, 且能自动处理 Cookie 的方式, 有时候我们不需要关心 Cookie 值是多少,
# 只是希望每次访问的时候, 程序自动把 Cookie 的值带上, 像浏览器一样. Requests 提拱了一个
# session 的概念, 在连续访问网页, 处理登录跳转时特别方便, 不需要关注具体细节. 使用方法示例如下:

# loginUrl = 'http://www.xxxxxx.com/login'
# s = requests.Session()
# # 首先访问登录界面, 作为游客, 服务器会先分配一个 cookie
# r = s.get(loginUrl, allow_redirects=True)
# datas = {'name': 'qiye', 'passwd': 'qiye'}
# # 向登录链接发送 post 请求, 验证成功, 游客权限转为会员权限.
# r = s.post(loginUrl, data=datas, allow_redirects=True)
# print(r.text)

# 上面的这段程序, 其实是正式做 Python 开发中遇到的问题, 如果没有第一步访问登录的
# 页面, 而是直接向登录链接发送 POST 请求, 系统会把你当做非法用户, 因为访问登录界面
# 时会分配一个 Cookie, 需要将这个 Cookie 在发送 POST 请求时带上, 这种使用 Session
# 函数处理 Cookie 的方式之后会很常用.

# 重定向与历史信息
# 处理重定向只是需要设置一下 allow_redirects 字段即可, 例如 r = requests.get(loginUrl, allow_redirects=True).
# 将 allow_redirects 设置为 True, 则是允许重定向; 设置为 False, 则是禁止重定向. 如果是允许重定向, 可以通过
# r.history 字段查看历史消息, 即访问成功之前的所有请求跳转信息. 示例如下:
# r = requests.get('http://github.com')
# print(r.url)
# print(r.status_code)
# print(r.history)
# 上面的示例代码显示的效果是访问 Github 网址时, 会将所有的 HTTP 请求全部重定向为 HTTPS.

# 超时设置
# 超时选项是通过参数 timeout 来进行设置的, 示例如下:
# requests.get('http://github.com', timeout=2)

# 代理设置
# 使用代理 Proxy, 你可以为任意请求方法通过设置 proxies 参数来配置单个请求:
# proxies = {
#     'http': 'http://0.10.1.10:3128',
#     'https': 'http://10.10.1.10:1080'
# }
# requests.get('http://example.org', proxies=proxies)
# 也可以通过环境变量 HTTP_PROXY 和 HTTPS_PROXY 来配置代理, 但是在爬虫开发中
# 不常用. 你的代理需要使用 HTTP Basic Auth, 可以使用http://user:password@host/语法:
proxies = {
    'http': 'http://user:pass@10.10.1.10:3128/'
}