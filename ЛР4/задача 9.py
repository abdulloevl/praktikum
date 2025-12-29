def safe_division_list(lst):
    results = []

    for item in lst:
        try:
            result = 100 / item
            results.append(result)
        except Exception as e:
            print("Ошибка:", e)

    return results


data = [10, 0, 5, "a", 20]
result = safe_division_list(data)

print("Результаты:", result)
