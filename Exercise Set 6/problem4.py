def make_repeater(func, n):
    def repeater(arg):
        for _ in range(n):
            arg = func(arg)
        return arg
    return repeater

def square(x):
    return x * x

# quadrupler = make_repeater(square, 4)

# print(quadrupler(2))

# single_square = make_repeater(square, 1)
# print(single_square(2))

# do_nothing = make_repeater(square, 0)
# print(do_nothing(5))