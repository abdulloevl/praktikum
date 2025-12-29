from collections import Counter

numbers = [1, 2, 3, 4, 5, 1, 6, 3]

counter = Counter(numbers)

duplicates = [num for num, count in counter.items() if count > 1]

unique_values = set(numbers)
unique_count = len(unique_values)

print("Исходный список:", numbers)
print("Повторяющиеся элементы:", duplicates)
print("Уникальные значения:", unique_values)
print("Количество уникальных значений:", unique_count)
