from log_system import log
from todo import Todo
from models import User
from path_fun import current_user


def template(name):
    path = 'templates/' + name
    log('path', path)
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


# 用于header的构造
def with_response_headers(headers, code=200):
    header = 'HTTP/1.1 {} Good\r\n'.format(code)
    log('header的值', header)
    # items() 函数以列表返回可遍历的(键, 值) 元组数组。
    header += ''.join('{}: {}\r\n'.format(k, v)
                     for k, v in headers.items())
    return header


# todo主页
def index(request):
    headers = {
        'Content-Type': 'text/html',
    }
    # 找到当前登录的用户, 如果没登录, 就 redirect 到 /login
    uname = current_user(request)
    u = User.find_by(username=uname)
    if u is None:
        return redirect('/login')
    todo_list = Todo.find_all(user_id=u.id)
    todos = []
    for t in todo_list:
        link = '<a href="/todo/show?id={}">编辑</a>'.format(t.id)
        todo_del = '<a href="/todo/del?id={}">删除</a>'.format(t.id)
        s = ''.join('<h3>{} : {} {} {}</h3>'.format(t.id, t.title, link, todo_del))
        todos.append(s)
    todo_html = ''.join(todos)
    body = template('todo_index.html')
    body = body.replace('{{todos}}', todo_html)
    header = with_response_headers(headers)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def add(request):
    """
    用于增加新的todo的路由函数
    """
    uname = current_user(request)
    u = User.find_by(username=uname)
    headers = {
        'Content-Type': 'text/html',
    }
    if request.method == 'POST':
        form = request.form()
        t = Todo.new(form)
        t.user_id = u.id
        t.save()
    return redirect('/todo')


def todo_show(request):
    headers = {
        'Content-Type': 'text/html',
    }
    uname = current_user(request)
    u = User.find_by(username=uname)
    if u is None:
        return redirect('/login')
    todo_id = int(request.query.get('id', -1))
    # 通过id查找整个字典
    t = Todo.find_by(id=todo_id)
    # 别的用户不能删除别人的微博
    if t.user_id != u.id:
        return redirect('/login')
    body = template('todo_edit.html')
    body = body.replace('{{todo_id}}', str(t.id))
    body = body.replace('{{todo_title}}', str(t.title))
    header = with_response_headers(headers)
    r = header + '\r\n' + body
    return r.encode('utf-8')


def update(request):
    """
        用于增加新的todo的路由函数
        """
    if request.method == 'POST':
        # 修改并且保存todo
        form = request.form()
        todo_id = int(form.get('id', -1))
        t = Todo.find_by(id=todo_id)
        t.title = form.get('title', t.title)
        t.save()
    # 浏览器发送数据过来被处理后, 重定向到首页
    # 浏览器在请求新首页的时候, 就能看到新增的数据了
    return redirect('/todo')


def todo__del(request):
    uname = current_user(request)
    u = User.find_by(username=uname)
    if u is None:
        return redirect('/login')
    todo_id = int(request.query.get('id', -1))
    t = Todo.find_by(id=todo_id)
    if t.user_id != u.id:
        return redirect('/login')
    if t is not None:
        t.remove()
    return redirect('/todo')


# 时未登录用户重定向
def redirect(url):
    """
       浏览器在收到 302 响应的时候
       会自动在 HTTP header 里面找 Location 字段并获取一个 url
       然后自动请求新的 url
    """
    headers = {
        'Location': url,
    }
    log('url是什么', url)
    # 增加 Location 字段并生成 HTTP 响应返回
    # 注意, 没有 HTTP body 部分
    r = with_response_headers(headers, 302) + '\r\n'
    log('r的值', r.encode('utf-8'))
    return r.encode(encoding='utf-8')


# 用于判定用户登陆，没登陆的会跳转
def login_required(route_function):
    def f(request):
        uname = current_user(request)
        u = User.find_by(username=uname)
        if u is None:
            return request('/login')
        return route_function(request)
    return f


todo_dict = {
    '/todo': index,
    '/todo/add': login_required(add),
    '/todo/show': todo_show,
    '/todo/update': update,
    '/todo/del': todo__del
}
