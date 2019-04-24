import time


def log(*args, **kwargs):
    form = '%Y/%m/%d/%H/%M/%S'
    value = time.localtime(time.time())
    t = time.strftime(form, value)
    print(t, *args, **kwargs)

