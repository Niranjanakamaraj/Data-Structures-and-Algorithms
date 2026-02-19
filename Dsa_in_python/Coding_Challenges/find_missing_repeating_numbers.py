def findRepeatingAndMissing(nums):
    n = len(nums)
    xor_all = 0
    for num in nums:
        xor_all ^= num
    for i in range(1, n + 1):
        xor_all ^= i
    set_bit = xor_all & -xor_all
    x = 0
    y = 0
    for num in nums:
        if num & set_bit:
            x ^= num
        else:
            y ^= num
    for i in range(1, n + 1):
        if i & set_bit:
            x ^= i
        else:
            y ^= i
    if nums.count(x) == 2:
        return [x, y]
    else:
        return [y, x]
