def Range(start, stop = None, step = None):
    if stop == None and step == None:
        stop = start
        start = 0
    if step == None:
        step = 1
    while start < stop:
        yield start
        start += step

# for i in Range(5):
#     print(i)
    
# for i in Range(0, 5):
#     print(i)
    
# for i in Range(0, 5, 2):
#     print(i)