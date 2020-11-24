import heapq

def huffman(heap):
    while len(heap) >= 2:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent_wt = left[0] + right[0]
        parent_name = left[1]+" "+right[1]
        heapq.heappush(heap, (parent_wt, parent_name))
        encode(left, right)

def encode(left, right):
    left_names = left[1].split()
    right_names = right[1].split()
    for left_name in left_names:
        if left_name in code:
            code[left_name] = '0' + code[left_name]
        else:
            code[left_name] = '0'
    for right_name in right_names:
        if right_name in code:
            code[right_name] = '1' + code[right_name]
        else:
            code[right_name] = '1'

code = {}
heap = []
#########Load File
file=open('huffman.txt')
data=file.readlines()
for i,line in enumerate(data):
    if i == 0:
        continue
    weight = int(line.strip())
    heapq.heappush(heap,(weight,str(i)))

huffman(heap)
code_list = sorted(list(code.values()),key = lambda x: len(x))
print('Maximum length of a codeword =',len(code_list[-1]))   #19
print('Minimum length of a codeword =',len(code_list[0]))    #9
