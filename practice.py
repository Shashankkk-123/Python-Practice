def sign_counters(nums):
    """Returns a 3-tuple containing the number of negative values in nums, 
    the number of zero values in nums and the number of positive values in nums."""
    result1 = result2 = result3 = 0
    for num in nums:
        if num > 0:
            result1 += 1
        if num < 0:
            result2 += 1
        if num == 0:
            result3 += 1
    return result1, result2, result3

print(sign_counters([-1, 2, 0, -3, -1, 0]))
print(sign_counters([-1, -5, -3, -2]))