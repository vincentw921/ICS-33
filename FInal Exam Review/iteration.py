class Range:
    def __init__(self, start, stop = None, step = None):
        if stop == None and step == None:
            stop = start
            start = 0
        if step == None:
            step = 1
        self.start = start
        self.stop = stop
        self.step = step
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start == self.stop:
            raise StopIteration()
        next = self.start
        self.start += self.step
        return next
    
# for i in Range(5):
#     print(i)
    
# for i in Range(1, 5):
#     print(i)
    
for i in Range(0, 6, 2):
    print(i)