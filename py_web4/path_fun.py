from log_system import log
from models.user import User
from models.message import Message
import random
import requests


def template(name):
    path = 'templates/' + name
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def route_index(request):
    header = 'HTTP/1.1 200 Good\r\nContent-Type: text/html\r\n'
    body = template('index.html')
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def current_user(request):
    session_id = request.cookies.get('user', '')
    # 把session键的值取出
    username = session.get(session_id, '【游客】')
    # username = request.cookies.get('user', '【游客】')
    return username


def response_with_headers(headers):
    """
  以下实现：
  content-Type: text/html
  set-Cookie: user=gua
    """
    # 原始响应行
    header = 'HTTP/1.1 210 Good\r\n'
    # Python 字典(Dictionary) items() 函数以列表返回可遍历的(键, 值) 元组数组,把headers以列表形式遍历
    header += ''.join(['{}: {}\r\n'.format(k, v)
                    for k, v in headers.items()])
    return header


# seesion可以在服务器端实现过期功能
session = {
    'username':
        {
            'username': 'peter',
            '过期时间': '4/30 22:25:00'
        }
}


def random_str():
    """
    生成一个随机字符串
    """
    seed = 'adhgfjkbmfdjkgfgfdldffgh15421gj54g2nf15f1f6'
    s = ''
    for i in range(16):
        random_index = random.randint(0, len(seed) - 2)
        s += seed[random_index]
        return s


# 用户登陆
def route_login(request):
    headers = {
        'Content-Type:': 'text/html',
    }
    log('requests and Cookie', headers, request.cookies)
    username = current_user(request)
    if request.method == 'POST':
        form = request.form()
        u = User.new(form)
        if u.validate_login():
            # 设置一个随机字符串来当令牌
            session_id = random_str()
            # 键是随机值，用户名是键（u.username）
            session[session_id] = u.username
            headers['Set-Cookie'] = 'user={}'.format(session_id)
            # 存在此用户后加上cookie
            # headers['Set-Cookie'] = 'user={}'.format(u.username)
            result = '登陆成功'
        else:
            result = '用户名或密码错误'
    else:
        result = ''
    body = template('login.html')
    body = body.replace('{{result}}', result)
    body = body.replace('{{username}}', username)
    header = response_with_headers(headers)
    log('header的值一', header)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


# 用户注册
def route_register(request):
    header = 'HTTP/1.1 200 Good\r\nContent-Type: text/html\r\n'
    if request.method == 'POST':
        form = request.form()
        u = User.new(form)
        if u.validate_register():
            log('这是判断--------')
            u.save()
            result = '注册成功<br> <pre>{}</pre>'.format(User.all())
        else:
            result = '用户名或者密码长度必须大于2'
    else:
        result = ''
    body = template('register.html')
    body = body.replace('{{result}}', result)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


# 用来存储message
message_list = []


# 消息页面的路由函数
def route_message(request):
    username = current_user(request)
    if username == '【游客】':
        log('**debug, route msg 未登陆')
    if request.method == 'POST':
        form = request.form()
        msg = Message.new(form)
        # msg加入message_list列表
        message_list.append(msg)
    header = 'HTTP/1.1 200 Good\r\nContent-Type: text/html\r\n'
    body = template('html_basic.html')
    # <br>是页面上的回车
    #  Python join() 方法用于将列表中的元素以指定的字符连接生成一个新的字符串
    msgs = '<br>'.join([str(m) for m in message_list])
    body = body.replace('{{messages}}', msgs)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')




def route_static(request):
    """
    读取图片并生成响应返回
    """
    filename = request.query.get('file', 'photo,jpg')
    path = 'photos/' + filename
    with open(path, 'rb') as f:
        header = b'HTTP/1.1 200 Good\r\nContent-Type: image/jpg\r\n'
        img = header + b'\r\n' + f.read()
        return img


route_dict = {
    '/': route_index,
    '/login': route_login,
    '/register': route_register,
    '/messages': route_message,
}