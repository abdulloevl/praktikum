from collections import deque

def sliding_avg(data, window_size):
    if not isinstance(window_size, int):
        raise TypeError("Размер окна должен быть целым числом")
    if window_size <= 0:
        raise ValueError("Размер окна должен быть больше 0")
    if len(data) < window_size:
        raise ValueError("Размер окна больше длины списка")
    window = deque()
    window_sum = 0
    for value in data:
        if not isinstance(value, (int, float)):
            raise TypeError("Элементы списка должны быть числами")
        window.append(value)
        window_sum += value
        if len(window) > window_size:
            window_sum -= window.popleft()
        if len(window) == window_size:
            yield window_sum / window_size
data = [1, 2, 3, 4]
window_size = 2
for avg in sliding_avg(data, window_size):
    print(avg)
