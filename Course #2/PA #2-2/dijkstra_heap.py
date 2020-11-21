import heapq
# from tqdm import tqdm

class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()
        self.dts =1000000  #distance to source

    def add_neighbor(self, v, weight):
        if v not in [row[0] for row in self.neighbors]:
            self.neighbors.append((v, weight))
            self.neighbors.sort()

class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v, weight=0):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbor(v, weight)
            self.vertices[v].add_neighbor(u, weight)
            return True
        else:
            print('Edge not added')
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key , self.vertices[key].neighbors)

    def dijkstra(self,s):
        X=[s]
        self.vertices[s].dts = 0
        pq = [(0,s)]
        while pq:
            pre_dist,v = heapq.heappop(pq)
            # Nodes can get added to the priority queue multiple times. We only
            # process a vertex the first time we remove it from the priority queue.
            if pre_dist > self.vertices[v].dts:
                continue
            for w,dist in self.vertices[v].neighbors:
                cur_dist = pre_dist + dist
                # Only consider this new path if it's better than any path we've
                # already found.
                if cur_dist < self.vertices[w].dts:
                    self.vertices[w].dts = cur_dist
                    heapq.heappush(pq,(cur_dist,w))
        a=[]
        for i in [7,37,59,82,99,115,133,165,188,197]:
            a.append(str(self.vertices[i].dts))
        print(','.join(a))

################load file
num_nodes = 200
g = Graph()
for i in range(1,num_nodes+1):
    g.add_vertex(Vertex(i))
with open('dijkstraData.txt') as file:
    for line in file:
        line = line.split()
        u=int(line[0])
        for v_dist in line[1:]:
            v_dist=v_dist.split(',')
            v=int(v_dist[0])
            dist=int(v_dist[1])
            # print(u,v,dist)
            g.add_edge(u,v,dist)
file.close()

# g.print_graph()
# print(g.vertices[1].neighbors)
g.dijkstra(1)
# 2599,2610,2947,2052,2367,2399,2029,2442,2505,3068
