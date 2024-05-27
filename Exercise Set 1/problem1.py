def only_truthy(**kwargs):
    truthy = {}
    for key, value in kwargs.items():
        if value:
            truthy[f'_{key}'] = value
    
    return truthy

# print(only_truthy(a = 0, b = 13, c = '', d = 'Boo'))
# print(only_truthy(name = 'Boo'))
# print(only_truthy())