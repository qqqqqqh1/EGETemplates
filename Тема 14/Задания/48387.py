def f(nums, base):
    return sum([nums[i] * base ** i for i in range(len(nums))])
for x in range(0, 11):
    for y in range(0, 11):
        x1 = f([x, 3, 4, 1, y][::-1], 11)
        x2 = f([5, 6, x, 1, y][::-1], 19)
        res = x1 + x2
        if res % 305 == 0:
            print(res // 305)