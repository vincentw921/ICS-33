class Vector:
    def __init__(self, *, x, y):
        self.x = x
        self.y = y
        
    def __getitem__(self, index):
        if index == 0:
            return self.x
        if index == 1:
            return self.y
        raise IndexError()
        
    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        if self.x == other.x and self.y == other.y:
            return True
        return False
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __lt__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x ** 2 + self.y ** 2 < other.x ** 2 + other.y ** 2
    
    def __neg__(self):
        return Vector(x=-self.x, y=-self.y)
    
    def __add__(self, other):
        return Vector(x=self.x + other.x, y=self.y + other.y)
    
    def __sub__(self, other):
        return Vector(x=self.x - other.x, y=self.y - other.y)
    
    def mult(self, other):
        if not isinstance(other, int) or not isinstance(other, float):
            return NotImplemented
        return Vector(x=other*self.x, y=other*self.y)