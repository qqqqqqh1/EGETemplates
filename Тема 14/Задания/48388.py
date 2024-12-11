def f(nums, base):
    nums = nums[::-1]
    return sum([nums[i] * base ** i for i in range(len(nums))])

for x in range(14):
    for y in range(14):
        x1 = f([x, 2, 3, 1, y], 12)
        x2 = f([7, 8, x, 9, 8, y], 14)
        res = x1 + x2
        if res % 99 == 0:
            print(res // 99)
            break