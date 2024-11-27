nums = list(map(int, open('37361.txt').readlines()))
cnt = 0
lst = []
for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if (nums[i] + nums[j]) % 126 == 0:
            cnt += 1
            lst.append(nums[i] + nums[j])
print(cnt, max(lst))