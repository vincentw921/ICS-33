class MultipleSequence:
    def __init__(self, len, multiplier = 1):
        self.len = len
        self.multiplier = multiplier
        
    def __len__(self):
        return self.len
    
    def __getitem__(self, index):
        if abs(index) >= self.len:
            raise IndexError()
        val = index * self.multiplier
        if index < 0:
            val += self.len * self.multiplier
        return val
            
    def __contains__(self, value):
        return value % self.multiplier == 0 and value / self.multiplier < self.len
    
sequence = MultipleSequence(5, 3)
print(list(sequence))