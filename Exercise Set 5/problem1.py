class MultipleSequence:
    
    class __MultipleSequenceIterator:
        def __init__(self, sequence):
            self.sequence = sequence
            self.index = 0
            
        def __next__(self):
            if self.index >= len(self.sequence):
                raise StopIteration
            value = self.sequence[self.index]
            self.index += 1
            return value
    
    def __init__(self, length, multiplier = 1, /):
        self.length = length
        if length < 0:
            raise ValueError
        
        self.multiplier = multiplier
        if type(multiplier) != int:
            raise ValueError
    
    def __len__(self):
        return self.length
    
    def __bool__(self):
        return self.length / self.multiplier != 0
    
    def __getitem__(self, index):
        if index < 0:
            index = len(self) + index
        if index < 0 or index >= len(self):
            raise IndexError
        return index * self.multiplier
    
    def __contains__(self, value):
        return value % self.multiplier == 0 and value / self.multiplier < self.length
    
    def __iter__(self):
        return self.__MultipleSequenceIterator(self)
    
    def __repr__(self):
        if self.multiplier == 1:
            return f"MultipleSequence({self.length})"
        return f"MultipleSequence({self.length}, {self.multiplier})"
    
def test_multiple_iter():
    
    s = MultipleSequence(5, 3)
    assert len(s) == 5
    assert bool(s) == True
    assert 0 in s
    assert 3 in s
    assert 6 in s
    assert 5 not in s
    assert 7 not in s
    assert s[0] == 0
    assert s[1] == 3
    assert s[-1] == 12
    assert s[-2] == 9
    assert list(s) == [0, 3, 6, 9, 12]
    
test_multiple_iter()