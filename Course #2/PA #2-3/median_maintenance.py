from heapq import heapify,heappush,heappop

hlow = []
heapify(hlow) #heap hlow stores smaller half (k+1)//2 of the data, pops max
hhi=[]
heapify(hhi) #heap hhi stores bigger half k-(k+1)//2 of the data, pops min
medians=[]

file = open("Median.txt", "r")
data = file.readlines()

for line in data:
    if not line.strip():
        continue
    cur_num = int(line.strip())
    # print(cur_num)
    if len(hlow) == 0 and len(hhi) == 0: #Case1: both hlow and hhi are empty, push to hlow
        heappush(hlow,-cur_num)
    elif len(hlow) != 0 and len(hhi) == 0: #Case2: hlow is not empty, hhi is empty
        if cur_num <= -hlow[0]:
            heappush(hlow,-cur_num)
        else:
            heappush(hhi,cur_num)
    else: #Case 3, both hlow and hhi are not empty
        if cur_num <= hhi[0]:
            heappush(hlow,-cur_num)
        else:
            heappush(hhi,cur_num)
    if len(hlow) > len(hhi)+1:
        heappush(hhi,-heappop(hlow))
    elif len(hlow) < len(hhi):
        heappush(hlow,-heappop(hhi))
    medians.append(-hlow[0])

print(sum(medians) % 10000)
