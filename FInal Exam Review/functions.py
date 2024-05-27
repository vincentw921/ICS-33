def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum

def get_vector(*, x, y):
    return (x, y)

def multiply(x, y, /):
    return x * y

def hashmap(**kwargs):
    return {x:kwargs[x] for x in kwargs}

print(get_vector(x=1, y=2))
print(add(1, 2, 3))
print(multiply(3, 5))

print(hashmap(x=1, y=2))