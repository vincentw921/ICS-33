def partially_call(f, *args, **kwargs):
    def complete_call(*args2, **kwargs2):
        return f(*(args + args2), **dict(kwargs, **kwargs2))
    return complete_call

def multiply(n, m):
    return n * m

def main():
    multiply_by_three = partially_call(multiply, 3)
    print(multiply_by_three(8)) # 24

    multiply_by_three_kw = partially_call(multiply, m = 3)
    print(multiply_by_three_kw(n = 8)) # 24
    print(multiply_by_three_kw(n = 8, m = 4)) # 32
    
    argless_multiply = partially_call(multiply, 3, 8)
    print(argless_multiply()) # 24
        
    # invalid_multiply = partially_call(multiply, q = 5)
    # invalid_multiply(n = 3, m = 7)
    
# main()