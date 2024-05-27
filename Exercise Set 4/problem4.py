import itertools

ar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tmp = list(itertools.islice(ar, 0, 10, 2))

tmp[0] = 0
print(ar)

ar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tmp = ar[0:10:2]

tmp[0] = 0
print(ar)