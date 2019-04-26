import json
from log_system import log


# 用于存储列表
def save(data, path):
    """
    本函数把一个 dict 或者 list 写入文件
    data 是 dict 或者 list
    path 是保存文件的路径
    """
    # json.dumps()函数是将字典转化为字符串
    # indent 是缩进
    # ensure_ascii=False 用于保存中文
    s = json.dumps(data, indent=2, ensure_ascii=False)
    with open(path, 'w+', encoding='utf-8') as f:
        log('save', path, s, data)
        f.write(s)


def load(path):
    """
    本函数从一个文件中载入数据并转化为 dict 或者 list
    path 是保存文件的路径
    """
    with open(path, 'r', encoding='utf-8') as f:
        s = f.read()
        log('load======', s)
        # json.loads是把字符串转成字典
        return json.loads(s)


class Model(object):
    # __name__这个系统变量显示了当前模块执行过程中的名称
    @classmethod
    # dp_path数据的存储位置类型
    def db_path(cls):
        # classmethod 有一个参数是 class
        # 所以我们可以得到 class 的名字
        classname = cls.__name__
        path = 'db/{}.txt'.format(classname)
        return path

    @classmethod
    # 用传来的数据，新建一个类
    def new(cls, form):
        # cls表示这个类本身,相当于 User(form)
        m = cls(form)
        return m

    @classmethod
    def all(cls):
        """
        得到一个类的所有存储实例
        """
        path = cls.db_path()
        log('path的值', path)
        # 得到path的数据后，用load载入数据
        # models被传入了很多字典的列表
        models = load(path)
        # 列表推导把每一个字典都传给一new函数，使他们变成对象而不是字典
        ms = [cls.new(m) for m in models]
        return ms

    def save(self):
        """
        用于把一个Model的实例保存到文件中
        """

        models = self.all()
        log('models', models)
        models.append(self)
        # __dict__ 是包含了对象所有属性和值的字典
        # 把所有的对象用字典表示 __dict__
        l = [m.__dict__ for m in models]
        path = self.db_path()
        save(l, path)

    def __repr__(self):
        # 得到类名
        classname = self.__class__.__name__
        # 可迭代对象
        properties = ['{}:({})'.format(k, v) for k, v in self.__dict__.items()]
        s = '\n'.join(properties)
        return '< {}\n{} >\n'.format(classname, s)




