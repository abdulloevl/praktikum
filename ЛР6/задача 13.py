def max_depth(lst):
    if not isinstance(lst, list):
        return 0
    if not lst:
        return 1
    return 1 + max(max_depth(item) for item in lst)
data = [1, [2, [3, [4]]]]
result = max_depth(data)
print("Максимальная глубина вложенности:", result)
