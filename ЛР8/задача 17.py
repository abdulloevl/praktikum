def min_sum_subarray_verbose(nums, k):
    if not isinstance(nums, list):
        raise TypeError("Ожидался список чисел")
    if k <= 0 or k > len(nums):
        raise ValueError("Некорректная длина окна")
    if not all(isinstance(x, (int, float)) for x in nums):
        raise TypeError("Все элементы nums должны быть числами")

 
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
