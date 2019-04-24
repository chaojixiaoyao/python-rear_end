import socket
import urllib.parse
from log_system import log
from path_fun import route_static
from path_fun import route_dict



# 定义一个类用来保存请求的数据
class Request(object):
    def __init__(self):
        self.method = 'GET'
        self.path = ''
        self.query = {}
        self.body = ''

    def form(self):
        """
                form 函数用于把 body 解析为一个字典并返回
                body 的格式如下 a=b&c=d&e=1
        """
        # unquote用于把url中一些不符合规范的字符转码，比如浏览器会把url中的空格变成%20
        # username=g+u%20a%3F&password=
        #  转成username=g u&a?&password=
        body = urllib.parse.unquote(self.body)
        log('此时的body', body)
        args = body.split('&')
        f = {}
        for arg in args:
            k, v = arg.split('=')
            f[k] = v
        return f


request = Request()


def error(request, code=404):
    e = {
        404: b'HTTP/1.1 404 Not Page\r\n\r\n<h1>Not Page</h1>',
    }
    return e.get(code, '')


def parse_path(path):
    index = path.find('?')
    if index == -1:
        return path, {}
    else:
        path, query_string = path.split('?', 1)
        args = query_string.split('&')
        query = {}
        for arg in args:
            k, v = arg.split('=')
            query[k] = v
        return path, query


def request_parse(path):
    # parse_path用于把path 和 query 分离
    path, query = parse_path(path)
    request.path = path
    request.query = query
    log('path and query', path, query)
    """
        根据 path 调用相应的处理函数
        没有处理的 path 会返回 404
    """
    lis_path = {
        '/photos': route_static

    }
    lis_path.update(route_dict)
    response = lis_path.get(path, error)
    return response(request)


def run(host='', port=2000):
    with socket.socket() as s:
        s.bind((host, port))
        while True:
            s.listen(5)
            content, addres = s.accept()
            r = content.recv(1000).decode('utf-8')
            log('r and addres, {}\n{}'.format(r, addres))
            # 防止客户端发送空请求导致程序崩溃
            if len(r.split()) < 2:
                continue
            path = r.split()[1]
            # 设置request的 method
            request.method = r.split()[0]
            request.body = r.split('\r\n\r\n', 1)[1]
            log("body的值", request.body)
            response = request_parse(path)
            content.sendall(response)
            content.close()


if __name__ == '__main__':
    config = dict(
        host='',
        port=2000,
    )
    run(**config)
