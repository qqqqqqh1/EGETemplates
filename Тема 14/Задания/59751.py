def f(nums, base):
    nums = nums[::-1]
    return sum([nums[i] * base ** i for i in range(len(nums))])

for x in range(19):
    x1 = f([7, 8, x, 7, 9, 6, 4, 3], 19)
    x2 = f([2, 5, x, 4, 3], 19)
    x3 = f([6, 3, x, 5], 19)
    res = x1 + x2 + x3
    if res % 18 == 0:
        print(res // 18)
        break