nums = list(map(int, open('61397.txt').readlines()))

def f(a, b, c):
    m = [len(str(a)), len(str(b)), len(str(c))]
    return m.count(4)
count = 0
maxlst = []
for num in nums:
    if num % 100 == 17:
        maxlst.append(num)
lst = []
for i in range(len(nums) - 2):
    if (f(nums[i], nums[i + 1], nums[i + 2]) == 2) and\
            ((nums[i] % 5 == 0) or (nums[i + 1] % 5 == 0) or (nums[i + 2] % 5 == 0)) and ((nums[i] + nums[i + 1] + nums[i + 2]) > max(maxlst)):
        count += 1
        lst.append(nums[i] + nums[i + 1] + nums[i + 2])
print(count, max(lst))