nums = list(map(int, open('hHTLyzmTi.txt').readlines()))
a = len(nums)
count = 0
lst = []
for i in range(len(nums) - 1):
    if (nums[i] < 0 or nums[i + 1] < 0) and (nums[i] + nums[i + 1]) < a and (nums[i] + nums[i + 1]) % 32 == 0:
        count += 1
        lst.append(nums[i] + nums[i + 1])
print(count, max(lst))