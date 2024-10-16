# Универсальное решение
# Вместо 15 может быть любая другая СС
def to_dec(nums, base):
    nums = nums[::-1]
    return sum([nums[i] * base ** i for i in range(len(nums))])


for x in range(15):
    x1 = to_dec([9, 8, x, 7, 9, 6, 4, 1], 22)
    x2 = to_dec([2, 5, x, 4, 9], 22)
    x3 = to_dec([6, 3, x, 5], 22)
    res = x1 + x2 + x3
    if res % 21 == 0:
        print(res // 21)
        break