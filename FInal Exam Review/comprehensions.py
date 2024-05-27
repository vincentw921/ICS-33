def multiples(count, multiplier):
    return [i * multiplier for i in range(1, count + 1)]

print(multiples(5, 6))
print(multiples(3, 5.5))
print(multiples(4, complex(1, 1)))