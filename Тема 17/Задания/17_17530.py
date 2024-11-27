nums = list(map(int, open('17_17530.txt').readlines()))
m = []
a = min(nums)
for i in range(len(nums) - 1):
    if (nums[i] % 55 == a or nums[i + 1] % 55 == a):
        m.append(nums[i] + nums[i + 1])
print(len(m), min(m))