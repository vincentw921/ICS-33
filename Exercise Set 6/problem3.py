def sequential_search(collection, target):
    if len(collection) == 0:
        return False
    
    iterator = iter(collection)
    
    def sequential_search_recursive(collection, target, iterator):
        try:
            if next(iterator) == target:
                return True
            return sequential_search_recursive(collection, target, iterator)
        except StopIteration:
            return False
    
    return sequential_search_recursive(collection, target, iterator)

"""
Closest Fit Run Time: O(n)
Closest Fit Space Complexity: O(n)
If python had tail call optimization, the space complexity would be O(1) because
the function would not need to store the recursive call in the call stack. Therefore,
the iterator variable would be updated and the function would be called again without
storing the previous call in the call stack.
"""
    
def binary_search(collection, target):
    if len(collection) == 0:
        return False    
    
    def binary_search_recursive(collection, target, start, end):
        if start > end:
            return False
        mid = (start + end) // 2
        if collection[mid] == target:
            return True
        elif collection[mid] < target:
            return binary_search_recursive(collection, target, mid + 1, end)
        else:
            return binary_search_recursive(collection, target, start, mid - 1)
        
    return binary_search_recursive(collection, target, 0, len(collection) - 1)

"""
Closest Fit Run Time: O(log n)
Closest Fit Space Complexity: O(log n)
If python had tail call optimization, the space complexity would be O(1) because the function
would not need to store the recursive call in the call stack. Therefore, the start and end
variables would be updated and the function would be called again without storing the previous
call in the call stack.
"""

# print(sequential_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)) # True
# print(sequential_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11)) # False

# print(sequential_search({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 5)) # True
# print(sequential_search({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 11)) # False

# print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)) # True
# print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11)) # False