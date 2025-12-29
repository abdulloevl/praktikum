def min_sum_subarray_verbose(nums, k):
    if not isinstance(nums, list):
        raise TypeError("Ожидался список чисел")
    if not isinstance(k, int):
        raise TypeError("k должен быть целым числом")
    if k <= 0 or k > len(nums):
        raise ValueError("Некорректная длина окна")
    if not all(isinstance(x, (int, float)) and x > 0 for x in nums):
        raise ValueError("Все элементы должны быть положительными числами")

   
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
