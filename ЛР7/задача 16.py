def min_sum_subarray_verbose(nums, k):
    if not isinstance(nums, list):
        raise TypeError("nums должен быть списком")
    if not all(isinstance(x, (int, float)) for x in nums):
        raise TypeError("Все элементы nums должны быть числами")
    if not isinstance(k, int):
        raise TypeError("k должен быть целым числом")
    if k <= 0:
        raise ValueError("k должен быть больше 0")
    if k > len(nums):
        raise ValueError("k не может быть больше длины списка")

    current_sum = sum(nums[:k])
    min_sum = current_sum
    print(f"Окно {nums[:k]} -> сумма = {current_sum}")

    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        min_sum = min(min_sum, current_sum)
        print(f"Окно {nums[i-k+1:i+1]} -> сумма = {current_sum}")

    print(f"Минимальная сумма подмассива длины {k} равна: {min_sum}")
    return min_sum

nums = [4, 2, 1, 7, 8, 1, 2, 6]
k = 3
min_sum_subarray_verbose(nums, k)
