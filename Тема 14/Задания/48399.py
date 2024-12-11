def f(nums, base):
    nums = nums[::-1]
    return sum([nums[i] * base ** i for i in range(len(nums))])

for x in range(16):
    x1 = f([3, 13, 4, x], 16)
    x2 = f([4, x, 12, 4], 14)
    res = x1 + x2
    if res % 154 == 0:
        print(res // 154)