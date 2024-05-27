class LimitingString:
    def __init__(self, limit, can_delete = False):
        if not isinstance(limit, int) or limit < 0:
            raise ValueError
        self.limit = limit
        
    def __get__(self, obj, objtype):
        return getattr(obj, self.value)
        
    def __set__(self, obj, value):
        setattr(obj, self.value, value)
        if not isinstance(value, str) or len(value) > self.limit:
            raise ValueError
        
    def __delete__(self, obj):
        if not self.can_delete:
            raise AttributeError
        delattr(obj, self.value)
        
class Thing:
    name = LimitingString(10)
    
t = Thing()
t.name = "Boo"
t.name = "Boo is perfect this afternoon"
t.name = 13
del t.name

