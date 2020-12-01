import sys
# import resource

sys.setrecursionlimit(3000)
items = [(0,0)]
book_keeper = {}
def knapsack(num,size):
    global book_keeper
    global items
    if book_keeper.get((num,size)) != None:
        return book_keeper[(num,size)]
    else:
        if size < items[num][1]:
            return knapsack(num-1 , size)
        else:
            best = max(knapsack(num-1,size),knapsack(num-1,size-items[num][1]) + items[num][0])
            book_keeper[(num,size)] = best
            return best

with open('knapsack_big.txt') as f:
    first_line = f.readline()[:-1]
    first_line = first_line.split()
    size, number_of_items = first_line
    data = f.readlines()
    for line in data:
        elements = list(map(int,line[:-1].split()))
        items.append((elements[0],elements[1]))
f.close()
for i in range(int(size)+1):
    book_keeper[(0,i)] = 0
print(knapsack(int(number_of_items),int(size)))
# 4243395
