import time

def with_time(f):
    def execute(*args, **kwargs):
        start = time.perf_counter()
        res = f(*args, **kwargs)
        print(f"Time spent: {time.perf_counter() - start}")
        return res
    return execute

@with_time
def square(n):
    time.sleep(10)
    return n * n

# print(square(10000))

def rate_limit(max_calls):
    class limit_calls:
        def __init__(self, func):
            self.func = func
            self.max_calls = max_calls
            
            self.total_calls = 0
            self.current_time = time.perf_counter()
            
        def __call__(self, *args, **kwargs):
            if self.total_calls > self.max_calls:
                raise ValueError()
            if time.perf_counter() - self.current_time > 1:
                self.current_time = time.perf_counter()
                self.total_calls = 0
            self.total_calls += 1
            return self.func(*args, **kwargs)
    return limit_calls
            

@rate_limit(5)
def square(n):
    return n * n

for i in range(10):
    print(square(5))