class Vector2D:
    def __init__(self, x, y, /):
        self.arg1 = x
        self.arg2 = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Vector3D(Vector2D):
    def __init__(self, x, y, z, /):
        super().__init__(x, y)
        self.z = z
    
    def getZ(self):
        return self.z
    
    def __eq__(self, other):
        if type(self) is not type(other):
            return False
        return super().__eq__(other) and self.z == other.z
    
    