nums = list(map(int, open('37336.txt.').readlines()))
maxlst = []
count = 0
for i in range(len(nums) - 1):
    if nums[i] % 3 == 0 or nums[i + 1] % 3 == 0:
        maxlst.append(nums[i] + nums[i + 1])
        count += 1
print(count, max(maxlst))