import random

def choose_random_key(G):
    # pick a random edge (u,v) from the graph G
    u = random.choice(list(G.keys()))
    v = random.choice(list(G[u]))
    return u,v

def kargerMinCut(file_path):
    ###Load Data###
    data = open(file_path,'r')
    G = {}
    for line in data:
        lst = [int(s) for s in line.split()]
        G[lst[0]] = lst[1:]

    # Shrink the graph G by one randomly picked edge (u,v) at a time ...
    # until there is only one edge left
    # The shrinking progress is to compress verticies u,v into one vertice u and ...
    # transfer v's neighbors to u, and ...
    # remove any cycles (e.g. u's neighbors being u) caused by the shrinking
    while len(G)>2:
        u,v = choose_random_key(G)
        G[u].extend(G[v]) # transfer v's neighbors to u
        for w in G[v]:
            G[w].remove(v) # To v's neighbors, update v to u as the neighbor
            G[w].append(u)
        while u in G[u]:
            G[u].remove(u) # remove cycles
        del G[v]
    return len(G[u])

def operation(n):
    # repeat the Karger Minimum Cut operation n times to get the Global Minimum
    # a single operation won't necessarily get to the Global Minimum due to random selection
    i = 0
    mincut = float('inf')
    while i < n:
        mincut = min(mincut,kargerMinCut("kargerMinCut.txt"))
        i += 1
        # print(mincut) # Uncomment this line to view the minimum cut progress
    return mincut

print(operation(100))
# 17
