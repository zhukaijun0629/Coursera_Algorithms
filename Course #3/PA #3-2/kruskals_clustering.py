import heapq
# from tqdm import tqdm

class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()
        self.dts = 1000000  #distance to source
        self.parent = n
        self.rank = 0

    def add_neighbor(self, v, weight):
        if v not in [row[0] for row in self.neighbors]:
            self.neighbors.append((v, weight))
            self.neighbors.sort()

class Graph:
    vertices = {}
    edges = []

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
            self.edges.append([u, v, weight])
            return True
        else:
            print('Edge not added')
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key , self.vertices[key].neighbors)

    def find(self,v):
        v_p = self.vertices[v].parent
        if v_p == v:
            return v
        return self.find(self.vertices[v_p].parent)

    def union(self,u,v):
        if u in self.vertices and v in self.vertices:
            #find u & v's parents and their ranks
            u_p = self.find(u)
            v_p = self.find(v)
            u_pr = self.vertices[u_p].rank
            v_pr = self.vertices[v_p].rank

        if u_pr == v_pr:
            #increase the rank by 1 for u's parent and
            #change v's parent's parent to u's parent
            self.vertices[u_p].rank += 1
            self.vertices[v_p].parent = u_p

        elif u_pr > v_pr:
            self.vertices[v_p].parent = u_p

        else:
            self.vertices[u_p].parent = v_p

    def primsMST(self,s):
        T = []
        X = [s]
        V = list(self.vertices.keys())
        edges = []
        for w,cost in self.vertices[s].neighbors:
            heapq.heappush(edges,(cost,w))
        while X != V:
            cheapest_cost,v = heapq.heappop(edges)
            # print(cheapest_cost,v)
            if v in X:
                continue
            T.append(cheapest_cost)
            X.append(v)
            X.sort()
            for w,cost in self.vertices[v].neighbors:
                heapq.heappush(edges,(cost,w))
        print(sum(T))

    def kruskalsClustering(self,num_nodes,k_target):
        k = num_nodes
        edges_order = sorted(self.edges, key = lambda x: x[2])

        while k != k_target:
            u,v,w = edges_order.pop(0)
            u_p = self.find(u)
            v_p = self.find(v)

            if u_p != v_p:
                self.union(u_p,v_p)
                k -= 1

        # within the edges left in edges_order,
        # find the next edge connecting two clusters, which has the max spacing
        while edges_order:
            u,v,w = edges_order.pop(0)
            u_p = self.find(u)
            v_p = self.find(v)
            if u_p != v_p:
                print(w)
                break

################load file
num_nodes = 500
g = Graph()
for i in range(1,num_nodes+1):
    g.add_vertex(Vertex(i))
file = open('clustering1.txt')
data = file.readlines()
for line in data[1:]:
    line = line.split()
    u = int(line[0])
    v = int(line[1])
    cost = int(line[2])
    g.add_edge(u,v,cost)

# g.print_graph()

g.kruskalsClustering(num_nodes,4)  #106
