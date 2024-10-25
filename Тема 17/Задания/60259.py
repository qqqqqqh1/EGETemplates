nums = list(map(int, open('60259.txt').readlines()))

def f(a,b,c):
    m = [len(str(a)),len(str(b)),len(str(c))]
    return m.count(3)

maxlst = []
lst = []
for num in nums:
    if num % 100 == 13:
        maxlst.append(num)
count = 0
maxnum = max(maxlst)
for i in range(len(nums) - 2):
    if (f(nums[i], nums[i + 1], nums[i + 2]) == 2) and (nums[i] + nums[i + 1] + nums[i + 2]) <= maxnum:
        count += 1
        lst.append(nums[i] + nums[i + 1] + nums[i + 2])
print(count, max(lst))