# Copyright David Bai: Anyone can use this code without permission or referencing the original source
# from tqdm import tqdm
"""
W1 Kosaraju Algorithm
List Based Iterative Implementation to find sizes of strongly connected components
"""

########################################################
# Data Structures

# node labels range from 1 to 875714. 875715 was used because of the range operator... range(875715) goes up to 875714.
num_nodes = 875715
# num_nodes = 13

# Adjacency representations of the graph and reverse graph
gr = [[] for i in range(num_nodes)]
r_gr = [[] for i in range(num_nodes)]

# The list index represents the node. If node i is unvisited then visited[i] == False and vice versa
visited = [False] * num_nodes

# The list below holds info about sccs. The index is the scc leader and the value is the size of the scc.
scc = [0] * num_nodes

stack = []  # Stack for DFS
order = []  # The finishing orders after the first pass


########################################################
# Importing the graphs
file = open("SCC.txt", "r")
data = file.readlines()

for line in data:
    if not line.strip():
        continue
    items = line.split()
    gr[int(items[0])] += [int(items[1])]
    r_gr[int(items[1])] += [int(items[0])]

# print(gr)
# print(r_gr)

########################################################
# DFS on reverse graph

# for node in tqdm(range(1,num_nodes)):
for node in range(1,num_nodes):
    if visited[node]==True:
        continue
    else:
        visited[node]=True
        stack.append(node)
    while stack:
        stack_node=stack[-1]
        if not r_gr[stack_node]:
            order.append(stack.pop())
        else:
            for head in r_gr[stack_node]:
                if visited[head]:
                    r_gr[stack_node].remove(head)
                    continue
                else:
                    stack.append(head)
                    r_gr[stack_node].remove(head)
                    visited[head]=True
                    break
# print(order)




########################################################
# DFS on original graph

visited = [False] * len(visited)  # Resetting the visited variable
order.reverse()  # The nodes should be visited in reverse finishing times
# print(order)

# for node in tqdm(order):
for node in order:
    temp=[]
    if visited[node]==True:
        continue
    else:
        visited[node]=True
        stack.append(node)
    while stack:
        stack_node=stack[-1]
        if not gr[stack_node]:
            temp.append(stack.pop())
        else:
            # gr[stack_node].sort(key=lambda x: order.index(x))
            for head in gr[stack_node]:
                if visited[head]:
                    gr[stack_node].remove(head)
                    continue
                else:
                    stack.append(head)
                    visited[head]=True
                    break
    scc[temp[-1]]=len(temp)
# print(scc)

########################################################
# Getting the five biggest sccs
scc.sort(reverse=True)
print(scc[:5])
