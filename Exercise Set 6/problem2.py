class HashableByAttributes:
    def __hash__(self):
        return hash(tuple(self._get_hashable_values()))
    
    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, type(self)):
            return False
        for i in self._get_hashable_keys():
            if self.__dict__[i] != __o.__dict__[i]:
                return False
        return True

    def _get_hashable_keys(self):
        for i in self.__dict__.keys():
            # isinstance(i, typing.Hashable)
            try:
                hash(self.__dict__[i])
                yield i
            except TypeError:
                continue
    
    def _get_hashable_values(self):
        for i in self.__dict__.values():
            # isinstance(i, typing.Hashable)
            try:
                hash(i)
                yield i
            except TypeError:
                continue
            
    
class Vector(HashableByAttributes):
    def __init__(self, position: list[int], velocity: list[int], speed: int):
        self.position = position
        self.velocity = velocity
        self.speed = speed
        
class Student(HashableByAttributes):
    def __init__(self, name: str, age: int, id: str, height: float):
        self.name = name
        self.age = age
        self.id = id
        self.height = height
        
# boo = Vector([1, 2, 3], [4, 5, 6], 5)
# other = Vector([1, 2, 3], [4, 5, 6], 2)
        
# print(boo == other)