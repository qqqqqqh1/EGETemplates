nums = list(map(int, open('55813.txt').readlines()))

def f(n):
    a = 0
    while n > 0:
        a += n % 10
        n //= 10
    return int(a)

count = 0
lst = []
lst1 = []
for num in nums:
    if (100 <= num < 1000) and (num % 10 == 5):
        lst.append(num)
min_num = min(lst)
for i in range(len(nums) - 1):
    if (100 <= nums[i] < 1000) != (100 <= nums[i + 1] < 1000) and (nums[i] + nums[i + 1]) % min_num == 0:
        count += 1
        lst1.append(nums[i] + nums[i + 1])
print(count, min(lst1))