def find_pair_with_sum(grades, target_sum):
    l = 0
    r = len(grades) - 1
    while l < r:
        current_sum = grades[l] + grades[r]
        if current_sum == target_sum:
            return grades[l], grades[r]
        elif current_sum < target_sum:
            l += 1
        else:
            r -= 1
    return None
grades = [2, 3, 4, 5, 7, 9, 12, 15]
target_sum = 16
result = find_pair_with_sum(grades, target_sum)
print(result)
