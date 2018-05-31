# httplib/urllib 实现
# httplib 模块是一个底层基础模块, 可以看到建立 HTTP 请求的每一步, 但是
# 实现的功能比较少, 正常情况下比较少用到. 在 Python 爬虫开发中基本上用不到,
# 所以在此只是进行一下知识普及. 下面介绍一下常用的对象函和函数:
# 1) 创建 HTTPConnection 对象: class httplib.HTTPConnection(host[,port[,strict[,timeout[,source_address]]]]).
# 2) 发送请求: HTTPConnection.request(method, url[,body[,headers]]).
# 3) 获得响应: HTTPConnection.getresponse().
# 4) 读取响应信息: HTTPConnection.read([amt]).
# 5) 获得指定头信息: HTTPConnection.getheader(name[,default]).
# 6) 获得相应头(header, value)元组的列表: HTTPConnection.getHeaders().
# 7) 获得底层 socket 文件描述符: HTTPConnection.fileno().
# 8) 获得头内容: HTTPConnection.msg.
# 9) 获得头 http 版本: HTTPConnection.version.
# 10) 获得返回状态码: HTTPConnection.status.
# 11) 获得返回说明: HTTPConnection.reason.

# 接下来演示一下 GET 请求和 POST 请求的发送,
# 首先是 GET 请求的示例, 如下所示:
import http.client
import urllib.parse

# conn = None
# try:
#     conn = http.client.HTTPConnection('www.baidu.com')
#     conn.request('GET', '/')
#     response = conn.getresponse()
#     print(response.status, response.reason)
#     print('-' * 40)
#     headers = response.getheaders()
#     for h in headers:
#         print(h)
#     print('-' * 40)
#     print(response.msg)
# except Exception as e:
#     print(e)
# finally:
#     if conn:
#         conn.close()


# POST 请求示例如下:

conn = None
try:
    params = urllib.parse.urlencode({'name': 'qiye', 'age': 22})
    headers = {
        'Content-type': 'application/x-www-form-urlencoded',
        'Accept': 'text/plain'
    }
    conn = http.client.HTTPConnection('www.zhihu.com', 80, timeout=3)
    conn.request('POST', '/login', params, headers)
    response = conn.getresponse()
    print(response.getheaders())
    print(response.status)
    print(response.read())
except Exception as e:
    print(e)
finally:
    if conn:
        conn.close()
