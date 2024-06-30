from master_linked_list import *
class Vertex1:
    def __init__(self,city_name):
        self.city = city_name
        #Linked list to store the users
        self.user_accounts = LinkedList()

    def element(self):
        return self.city
    
    
    def __hash__(self):
        return hash(id(self))
    

class Edge1:

    def __init__(self,u,v,x):
        self.origin = u
        self.destination = v
        self.weight = x

    def endpoints(self):
        return (self.origin,self.destination)
    
    def getweight(self):
        return self.weight
    
    def opposite(self,v):
        return self.destination if v is self.origin else self.origin
    
    def __str__(self):
        return f"{self.origin.city} ----{self.weight}-----> {self.destination.city}"
    
class Graph1:
    def __init__(self,directed=False):
        self.outgoing = {}
       
        self.incoming = {} if directed else self.outgoing
    
    def is_directed(self):
        return self.incoming is not self.outgoing
    
    def vertices(self):
        return self.outgoing.keys()
    
    
    def edges(self):
        result = set()
        for secondary_map in self.outgoing.values():
            result.update(secondary_map.values())
        return result
    
    def get_edge(self,u,v):
        return self.outgoing[u].get(v)
    
    def get_vertex(self,u):
        for i in self.outgoing:
            if i.city == u:
                return i
            
    
    def insertVertex(self,cityname):
       
        v = Vertex1(cityname)
        self.outgoing[v] = {}
        if self.is_directed():
            self.incoming[v] = {}
        return v
    
    def insert_edge(self,u1,v1,x=None):
        u = self.get_vertex(u1)
        v = self.get_vertex(v1)
        e = Edge1(u,v,x)
        self.outgoing[u][v] = e
        if self.is_directed():
            return
        self.incoming[v][u] = e

    def remove_edge(self,u1,v1):
        u = self.get_vertex(u1)
        v = self.get_vertex(v1)
        self.outgoing[u].pop(v)
        if self.is_directed():
            return
        self.incoming[v].pop(u)

    def remove_vertex(self,u1):
        u = self.get_vertex(u1)
        self.outgoing.pop(u)
        if self.is_directed():
            return
        for key,value in self.outgoing.items():
            if value and u in value:
                del self.outgoing[key][u]

    def incident_edges(self,v1,outgoing=True):
        adj = self.outgoing if outgoing else self.incoming
        v = self.get_vertex(v1)
        for edge in adj[v].values():
            yield edge
        
    def vertices_count(self):
        return len(self.outgoing)
    
    
def DFS(g, u, discovered):
    for e in g.incident_edges(u.element):
        v = e.opposite(u)
        if v not in discovered:
            discovered[v] = e
            DFS(g,v,discovered)
def BFS(g, s, discovere_bfs):
    level = [s]
    while len(level) > 0:
        next_level = []
        for u in level:
            for e in g.incident_edges(u):
                v = e.opposite(u)
                if v  not in discovere_bfs:
                    discovere_bfs[v] = e
                    next_level.append(v)
        level = next_level

def construct_path(u,v,discovered):
    path = []
    if v in discovered:
        path.append(v)
        walk = v
        while walk is not u:
            e = discovered[walk]
            parent = e.opposite(walk)
            path.append(parent)
            walk = parent
        path.reverse()
    return path

def test_connectivity(g,discovered):
    return len(discovered) == g.vertices_count()




