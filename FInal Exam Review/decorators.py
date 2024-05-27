import time

def hash_args(*args, kwargs):
    return hash(tuple(*args))

def cached(size):
    cache = {}
    def decorator(f):
        def func(*args, **kwargs):
            if tuple(args) in cache:
                return cache[tuple(args)]
            res = f(*args, **kwargs)
            cache[tuple(args)] = res
            return res
        return func
    return decorator

@cached(20)
def expensive_square(n):
    time.sleep(10)
    return n * n

print(expensive_square(5))
print(expensive_square(5))


def fields(field_names):
    field_names = list(field_names)
    
    def make_field_getter(field_name):
        def get_field(self):
            return getattr(self, f'_{field_name}')
        return get_field
    
    def decorate(cls):
        for field_name in field_names:
            setattr(cls, field_name, make_field_getter(field_name))
        
        def __init__(self, *args):
            for field_name, arg in zip(field_name, args):
                setattr(self, f'_{field_name}', arg)
                
        cls.__init__ == __init__
        return cls
    return decorate