def f(nums, base):
    nums = nums[::-1]
    return sum([nums[i] * base ** i for i in range(len(nums))])

for x in range(15):
    x1 = f([4, 12, x, 4], 15)
    x2 = f([x, 6, 2, 10], 13)
    res = x1 + x2
    if res % 121 == 0:
        print(res // 121)