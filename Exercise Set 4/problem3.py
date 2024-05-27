def generate_range(start, end, step):
    while start < end:
        yield start
        start += step
        
class Range:
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start < self.end:
            result = self.start
            self.start += self.step
            return result
        else:
            raise StopIteration