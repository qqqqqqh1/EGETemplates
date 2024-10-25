nums = list(map(int, open('37369.txt').readlines()))
count = 0
lst = []
for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if abs(nums[i] - nums[j]) % 80 == 0:
            count += 1
            lst.append(abs(nums[i] - nums[j]))
print(count, max(lst))