nums = list(map(int, open('39763.txt').readlines()))
count = 0
lst = []
for i in range(len(nums) - 2):
    f = sorted([nums[i], nums[i + 1], nums[i + 2]])
    if f[2] ** 2 < f[1] ** 2 + f[0] ** 2:
        count += 1
        lst.append(nums[i] + nums[i + 1] + nums[i + 2])
print(count, max(lst))