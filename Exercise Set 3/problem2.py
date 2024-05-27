def multiples(count, multiplier):
    return [i * multiplier for i in range(1, count + 1)]

def with_non_zero_lengths(*args):
    return {arg: len(arg) for arg in args if len(arg) > 0}

def make_diagonal(n):
    return [["B" if i == j else None for j in range(n)] for i in range(n)]

# print(multiples(5,6))
# print(multiples(3, 5.5))
# print(multiples(4, complex(1, 1)))

# print(with_non_zero_lengths())
# print(with_non_zero_lengths('Boo', 'is', 'happy'))
# print(with_non_zero_lengths(range(3), range(0), range(1)))

# print(make_diagonal(1))
# print(make_diagonal(3))