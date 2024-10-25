nums = list(map(int, open('39246.txt').readlines()))

count = 0
lst = []
for i in range(len(nums) - 1):
    if (nums[i] % 5 == 0 or nums[i + 1] % 5 == 0) and ((nums[i] + nums[i + 1]) % 7 == 0):
        count += 1
        lst.append(nums[i] + nums[i + 1])
print(count, max(lst))