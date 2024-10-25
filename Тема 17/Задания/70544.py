nums = list(map(int, open('70544.txt').readlines()))
min_num = min(nums)
lst = []
count = 0
for i in range(len(nums) - 1):
    if (nums[i] % 16 == min_num) or (nums[i + 1] % 16 == min_num):
        count += 1
        lst.append(nums[i] + nums[i + 1])
print(count, max(lst))