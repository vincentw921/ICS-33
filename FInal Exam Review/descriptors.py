import datetime

class ImmutableValue:
    def __set_name__(self, cls, name):
        self.name = f"_{name}"
        
    def __get__(self, obj, objtype):
        if obj is not None:
            return getattr(obj, self.name)
        else:
            return self
    
    def __set__(self, obj, value):
        if obj is not None:
            raise AttributeError()
        
    def __del__(self, obj, value):
        if obj is not None:
            raise AttributeError()
        
class Person:
    name = ImmutableValue()
    birthdate = ImmutableValue()
    
    def __init__(self, name, birthdate):
        self._name = name
        self._birthdate = birthdate
        
# p = Person("boo", 69699)
# print(p.name)
# print(p.birthdate)

class LimitedString:
    def __init__(self, len, can_delete=False):
        self.max_len = len
        self.can_delete = can_delete
        
    def __set_name__(self, obj, name):
        self.name = f"_{name}"
        
    def __get__(self, obj, objtype):
        if obj is not None:
            return getattr(obj, self.name)
        
    def __set__(self, obj, value):
        if obj is not None:
            if not isinstance(value, str) or len(value) > self.max_len:
                raise ValueError()
            setattr(obj, self.name, value)
            
    def __delete__(self, obj):
        if obj is not None:
            if self.can_delete:
                delattr(obj, self.name)
            else:
                raise AttributeError()

class Thing:
    name = LimitedString(10, can_delete=True)
    
t = Thing()
t.name = 'Boo'
print(t.name)
# t.name = 'Boo is perfect this afternoon'
# t.name = 13
del t.name