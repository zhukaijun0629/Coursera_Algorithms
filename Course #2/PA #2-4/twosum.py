# from tqdm import tqdm
from collections import defaultdict

file = open('algo1-programming_prob-2sum.txt')
data = file.readlines()
nums = defaultdict(list)
count = 0
res = set()

for line in data:
    if not line.strip():
        continue
    num = int(line.strip())
    nums[num//10000].append(num)
    # Generate hashtable such that each buckets contains numbers with the same ...
    # digits except last 4

# print(nums)

# for key1,xs in tqdm(nums.items()):
for key1,xs in nums.items():
    # for a number x in bucket1, the other number y could only be found in the following buckets
    for key2 in range(-int(key1) - 2, -int(key1) + 1):
        if key2 in nums.keys():
            for x in xs:
                for y in nums[key2]:
                    if abs(x+y) < 10000:
                        res.add(x + y)

print(len(res))
# 427
