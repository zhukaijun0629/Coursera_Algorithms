import heapq
# from tqdm import tqdm

class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()
        self.dts = 1000000  #distance to source

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

    def primsMST(self,s):
        T = []
        X = [s]
        V = list(self.vertices.keys())
        edges = []
        for w,cost in self.vertices[s].neighbors:
            heapq.heappush(edges,(cost,w))
        while X != V:
            cheapest_cost,v=heapq.heappop(edges)
            # print(cheapest_cost,v)
            if v in X:
                continue
            T.append(cheapest_cost)
            X.append(v)
            X.sort()
            for w,cost in self.vertices[v].neighbors:
                heapq.heappush(edges,(cost,w))
        print(sum(T))




################load file
num_nodes = 500
g = Graph()
for i in range(1,num_nodes+1):
    g.add_vertex(Vertex(i))
file = open('edges.txt')
data = file.readlines()
for line in data[1:]:
    line = line.split()
    u = int(line[0])
    v = int(line[1])
    cost = int(line[2])
    g.add_edge(u,v,cost)


# g.print_graph()

# print(g.vertices[1].neighbors)
g.primsMST(1)
# -3612829
