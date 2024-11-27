nums = list(map(int, open('17.txt').readlines()))
m = min(nums)
lst = []
for i in range(len(nums) - 1):
    if nums[i] % 18 + nums[i + 1] % 18 == m:
        lst.append(nums[i] + nums[i + 1])
print(len(lst), max(lst))
