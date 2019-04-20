import socket


host = ''
port = 2000

# s 是一个 socket 实例
s = socket.socket()
# s.bind 用于绑定
s.bind((host, port))


# 用一个无限循环来处理请求
while True:
    # 先要 s.listen 开始监听
    s.listen(5)
    # 当有客户端过来连接的时候, s.accept 函数就会返回 2 个值
    # 分别是 连接 和 客户端 ip 地址
    connection, address = s.accept()

    # recv 可以接收客户端发送过来的数据
    # 参数是要接收的字节数
    # 返回值是一个 bytes 类型
    request = connection.recv(1024)

    # bytes 类型调用 decode('utf-8') 来转成一个字符串(str)
    print('ip and request, {}\n{}'.format(address, request.decode('utf-8')))

    # b'' 表示这是一个 bytes 对象
    response = b'HTTP/1.1 200 GOOD\r\n\r\n<h1>Hello World!</h1>'
    print(response)
    # 用 sendall 发送给客户端
    connection.sendall(response)
    # 发送完毕后, 关闭本次连接
    connection.close()

