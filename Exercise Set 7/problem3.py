import random
import time

def hash_args(args, kwargs):
    for k, v in sorted(kwargs.items()):
        args += (k, v)
    return tuple(args)

def cached(size):
    def decorator(func):
        cache = {}
        def wrapper(*args, **kwargs):
            key = hash_args(args, kwargs)
            if key in cache:
                return cache[key]
            else:
                if len(cache) >= size:
                    del cache[random.choice(list(cache.keys()))]
                cache[key] = func(*args, **kwargs)
                return cache[key]
        return wrapper
    return decorator

@cached(2)
def expensive_square(n):
    time.sleep(5)
    return n*n

@cached(2)
def expensive_add(a, b):
    time.sleep(5)
    return a+b

@cached(2)
def expensive_divide(divident, divisor):
    time.sleep(5)
    return divident/divisor

def main():
    print(expensive_square(3))
    print(expensive_square(4))
    print("Sleeping for 5 seconds")
    print(expensive_square(3))
    print("Overwriting the cache")
    print(expensive_square(5))
    print(expensive_square(4))
    print(expensive_square(3))
    print(expensive_square(5))
    
    print(expensive_add(3, 4))
    print(expensive_add(4, 5))
    print("Sleeping for 5 seconds")
    print(expensive_add(3, 4))
    
    print(expensive_divide(divident=3, divisor=4))
    print(expensive_divide(divident=4, divisor=5))
    print("Sleeping for 5 seconds")
    print(expensive_divide(divident=3, divisor=4))
    
# main()