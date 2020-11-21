# from tqdm import tqdm

class Vertex:
    def __init__(self, n):
        self.name = n
        self.parent = n
        self.rank = 0

class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False


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

    def invert(self,bit):
        if bit != '0' and bit != '1':
            raise ValueError
        return '1' if bit == '0' else '0'

    def similar(self,v):
        out = []
        for i in range(len(v)):
            out.append(v[:i]+self.invert(v[i]) + v[i+1:])
            for j in range(i+1, len(v)):
                out.append(v[:i]+self.invert(v[i])+v[i+1:j]+self.invert(v[j])+v[j+1:])
        return out

    def clustering(self):
        # for u in tqdm(self.vertices):
        for u in self.vertices:
            u_p = self.find(u)

            for v in self.similar(self.vertices[u].name):
                if v in self.vertices:
                    v_p = self.find(v)
                    if v_p != u_p:
                        self.union(u,v)

        print(len(set(map(self.find,self.vertices))))




################load file
num_nodes = 200000
g = Graph()
file=open('clustering_big.txt')
data=file.readlines()
for line in data[1:]:
    u = "".join(line.split(' ')).strip()
    g.add_vertex(Vertex(u))

g.clustering()
# 6118
