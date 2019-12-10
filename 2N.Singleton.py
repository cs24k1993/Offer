# coding: utf-8
'''
单例模式,核心结构中只包含一个被称为单例类的特殊类,类的对象只能存在一个
三个要点: 某个类只有一个实例; 必须自行创建这个实例; 必须自行向整个系统提供这个实例
'''
'''
方法1: 实现__new__方法,然后将类的一个实例绑定到类变量 instance上
如果cls.instance为None, 说明该类没有被实例化过, new一个该类的实例,并返回
如果cls.instance不是None, 直接返回instance
'''
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        # 关键在于这，每一次实例化的时候，我们都只会返回这同一个instance对象
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton,cls).__new__(cls,*args,**kwargs)
            # orig = super(Singleton, cls)  也可以这样写
            # cls.instance = orig.__new__(cls, *args, **kwargs)
        return cls.instance

class Myclass(Singleton):
    a = 1

#下面两句有什么效果？
one = Myclass()
two = Myclass()

# one和two完全相同, 可以用id(), ==, is检测
print(id(one))
print(id(two))
print(one == two)       # True
print(one is two)       # True

two.a = 3
print(one.a)    # 3
