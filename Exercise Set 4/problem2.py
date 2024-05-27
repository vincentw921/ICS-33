def generate_range(start, end=None, step=1):
    if end is None:
        start, end = 0, start
    if step == 0:
        raise ValueError("Step must be non-zero")

    while start < end:
        yield start
        start += step
        
def no_fizz_without_buzz(value):
    while True:
        if value % 3 == 0 and value % 5 == 0 or (value % 3 != 0 and value % 5 != 0):
            yield value
        value += 1
    
def cartesian_product(*lists):
    iterators = [0] * len(lists)
    while True:
        yield tuple(lists[i][iterators[i]] for i in range(len(lists)))
        iterators[len(lists) - 1] += 1
        for i in range(len(lists) - 1, -1, -1):
            if iterators[i] == len(lists[i]) and i != 0:
                iterators[i] = 0
                iterators[i - 1] += 1
            if iterators[i] == len(lists[i]) and i == 0:
                return
            
def test_cartesian_product():
    assert list(cartesian_product([1, 2], [3, 4])) == [(1, 3), (1, 4), (2, 3), (2, 4)]
    assert list(cartesian_product([1, 2], [3, 4], [5, 6])) == [(1, 3, 5), (1, 3, 6), (1, 4, 5), (1, 4, 6), (2, 3, 5), (2, 3, 6), (2, 4, 5), (2, 4, 6)]
    assert list(cartesian_product([1, 2], [3, 4], [5, 6], [7, 8])) == [(1, 3, 5, 7), (1, 3, 5, 8), (1, 3, 6, 7), (1, 3, 6, 8), (1, 4, 5, 7), (1, 4, 5, 8), (1, 4, 6, 7), (1, 4, 6, 8), (2, 3, 5, 7), (2, 3, 5, 8), (2, 3, 6, 7), (2, 3, 6, 8), (2, 4, 5, 7), (2, 4, 5, 8), (2, 4, 6, 7), (2, 4, 6, 8)]
    
def test_generate_range():
    for i, value in enumerate(generate_range(1, 10, 2)):
        assert value == 1 + 2 * i

def test_no_fizz_without_buzz():
    for i, value in enumerate(no_fizz_without_buzz(1)):
        if i == 100:
            break
        if value % 3 == 0 and value % 5 == 0:
            assert True
        if value % 3 != 0 and value % 5 != 0:
            assert True
        if value % 3 == 0 and value % 5 != 0:
            assert False
        if value % 3 != 0 and value % 5 == 0:
            assert False
    assert True
        
# test_cartesian_product()
# test_no_fizz_without_buzz()
# test_generate_range()
# print(list(generate_range(1, 10, 2)))