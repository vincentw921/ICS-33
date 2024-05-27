def biiterate(items):
    iterator1 = iter(items)
    i = 0
    while True:
        try:
            value2 = next(iterator1)
        except StopIteration:
            return
        iterator2 = iter(items)
        j = 0
        while j <= i:
            yield (next(iterator2), value2)
            j += 1
        i += 1
        
print(list(biiterate(range(4))))