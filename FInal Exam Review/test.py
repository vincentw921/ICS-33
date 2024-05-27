class ImmutableValue:
    def __set_name__(self, cls, name):
        self._name = f"_{name}"
        
    def __get__(self, obj, objtype):
        if obj is None:
            return self
        return getattr(obj, self._name)
    
    # def __getattr__(self, obj, objtype):
    #     if obj is None:
    #         return self
    #     return getattr(obj, self._name)
    
class Person:
    name = ImmutableValue()
    birthdate = ImmutableValue()
    
    def __init__(self, name, birthdate):
        self._name = name
        self._birthdate = birthdate
        
boo = Person("Boo", 12344)
# print(boo.name)
