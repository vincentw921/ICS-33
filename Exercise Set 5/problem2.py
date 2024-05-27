class Collection:
    def __init__(self, values):
        self._values = values
        
    def __eq__(self, __o: object):
        if not isinstance(__o, Collection):
            return False
        for i in range(min(len(self._values), len(__o._values))):
            if self._values[i] != __o._values[i]:
                return False
        return len(self._values) == len(__o._values)
    
    def __lt__(self, __o: object):
        if not isinstance(__o, Collection):
            return False
        for i in range(min(len(self._values), len(__o._values))):
            if self._values[i] > __o._values[i]:
                return False
        if len(self._values) > len(__o._values):
            return False
        return True

def test_collection():
    c = Collection([1, 2, 3])
    d = Collection([1, 2, 3])
    assert c == d
    d = Collection([1, 2, 4])
    assert c < d
    d = Collection([1, 2, 3, 4])
    assert c < d
    c = Collection([1, 2, 3, 4])
    d = Collection([1, 2, 3])
    assert c > d
    
test_collection()