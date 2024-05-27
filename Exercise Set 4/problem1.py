class all_substring:
    def __init__(self, string):
        self.string = string
        self.start = 0
        self.end = 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        next_value = self.string[self.start:self.end]
        if self.end >= len(self.string):
            self.start += 1
            self.end = self.start
        if self.start > len(self.string):
            raise StopIteration
        else:
            self.end += 1
            return next_value
        
def all_substrings(string):
    return all_substring(string)

def test_all_substrings():
    assert list(all_substrings("abc")) == ["a", "ab", "abc", "b", "bc", "c"]
    assert list(all_substrings("ab")) == ["a", "ab", "b"]
    assert list(all_substrings("a")) == ["a"]
    assert list(all_substrings("")) == []
    
# test_all_substrings()
# print(list(all_substrings("abc")))