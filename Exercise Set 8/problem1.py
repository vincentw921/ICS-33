class class_method:
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, objtype):
        def new_f(*args, **kwargs):
            return self.f(objtype, *args, **kwargs)
        return new_f
    
class Thing:
    @class_method
    def foo(cls, x, y):
        return (cls.__name__, x + y)
    
# print(Thing.foo(1, 2))  # ('Thing', 3)
# print(Thing().foo(1, 2))  # ('Thing', 3)