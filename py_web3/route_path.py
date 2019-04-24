


def open_name(name):
    path = 'templates/' + name
    with open(name, 'rb', encoding='utf-8') as f:
        return f.read()

def route_register(request):
    header = 'HTTP/1.1 200 Good\r\nContent-Type: text/html\r\n'
    if request.method == 'POST':



d = {
    '/register': route_register,
}