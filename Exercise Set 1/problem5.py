class WrongException(Exception):
    pass

class ExceptionManager:
    def __init__(self, exception):
        self.exception = exception
        
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            raise WrongException('No exception raised')
        if exc_type is not self.exception:
            raise WrongException('Wrong exception raised')
        return True
        

def should_raise(exception):
    return ExceptionManager(exception)
        

# with should_raise(ValueError):
#     int('Boo')

# with should_raise(IndexError):
#     x = [1, 2, 3]
#     x[0]

# with should_raise(ValueError):
#     x = [1, 2, 3]
#     x[10]