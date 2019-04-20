import socket
import time


def log(*args, **kwargs):
    format = '%Y/%m/%d/%M/%S'
    value = time.localtime(time.time())
    t = time.strftime(format, value)
    print(t, *args, **kwargs)


def error(code=404):
    e = {
        404: b'HTTP/1.1 404 error page\r\n\r\n<h1>error page</h1>'
    }
    response = e.get(code, b'')
    return response


def route_index():
    headers = 'HTTP/1.1 200 Good\r\nContent-Type:text/html\r\n'
    # 想显示的都要加入body，写标签放置
    body = '<h1>hello world</h1><img src="feng.webp">'
    r = headers + '\r\n' + body
    # 指定编码格式encode, encoding=设置编码格式
    return r.encode(encoding='utf-8')


def route_image():
    # 打开图片
    with open('feng.webp', 'rb')as f:
        header = b'HTTP/1.1 200 Good\r\nContent-Type: image/webp\r\n'
        img = header + b'\r\n' + f.read()
        return img


def web_hl():
    # 打开本地html文件
    with open('html_show.html', encoding='utf-8') as f:
        fp = f.read()
    header = 'HTTP/1.1 200 good\r\nContent-Type: text/html\r\n'
    r = header + '\r\n' + fp
    return r.encode(encoding='utf-8')


def request_parse(path):
    li = {
        '/': route_index,
        '/feng.webp': route_image,
        '/hl': web_hl,
    }
    response = li.get(path, error)
    return response()


def run(host='', port=2000):
    with socket.socket() as s:
        s.bind((host, port))
        while True:
            s.listen(5)
            # content 存储了原始请求
            content, addres = s.accept()
            request = content.recv(1024).decode('utf-8')
            log('request and addres,{}\n{}'.format(request, addres))
            try:
                path = request.split()[1]
                response = request_parse(path)
                content.sendall(response)
            except Exception as e:
                log('error', e)
                content.close()


def main():
    config = dict(
        host='',
        port=2000,
    )
    run(**config)


if __name__ == '__main__':
    main()


