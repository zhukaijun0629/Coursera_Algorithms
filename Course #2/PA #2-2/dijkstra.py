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
        target = sorted(list(self.vertices.keys()))
        while X != target:
            min_dist=float('inf')
            for v in X:
                pre_dist = self.vertices[v].dts
                for w,dist in self.vertices[v].neighbors:
                    if w not in X:
                        cur_dist = pre_dist + dist
                        if cur_dist < min_dist:
                            min_dist=cur_dist
                            close_nb=w
                            # print(closest_nb, self.vertices[closest_nb].dts)
            X.append(close_nb)
            X.sort()
            self.vertices[close_nb].dts=min_dist
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
