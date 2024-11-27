nums = list(map(int, open('ztWdk3xW5.txt').readlines()))
count = 0
lst = []
for i in range(len(nums) - 1):
    for c in range(100, 5001):
        if nums[i] % c == 0 and nums[i + 1] % c == 0:
            lst.append(abs(nums[i] - nums[i + 1]))
            count += 1
print(count, max(lst))