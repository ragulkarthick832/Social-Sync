from master_linked_list import *
import networkx as nx
import matplotlib.pyplot as plt
import random
class Vertex:
    def __init__(self,user_id,password=None,name=None,age=None,gender=None,phone=None,email_id=None,location=None,interest=None):
         self.userid = user_id
         self.name = name
         self.age = age
         self.gender = gender
         self.phone = phone
         self.email_id = email_id
         self.location = location
         self.interests = interest
         self.password = password
         self.message = None

    def element(self):
        return self.userid
    
    
    def __hash__(self):
        return hash(id(self))
    
    def __str__(self):
        return f"{self.userid}"
    
    
    

class Edge:
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
        return f"{self.origin.name} ----{self.weight}-----> {self.destination.name}"
    
class Graph:
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
            if i.userid == u:
                return i
            
    
    def insertVertex(self,user_name,password,name,age,gender,phone,email_id,location,interest):
       
        v = Vertex(user_name,password,name,age,gender,phone,email_id,location,interest)
        self.outgoing[v] = {}
        if self.is_directed():
            self.incoming[v] = {}
        return v
    
    def insert_edge(self,u1,v1,x=None):
        u = self.get_vertex(u1)
        v = self.get_vertex(v1)
        e = Edge(u,v,x)
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
    
    def addMessage(self,vertex,msg):
        vertex.message = msg
    
    # Function to detect cycle between two vertices
    # O(V+E)
    def detect_cycle_between(self, start, end):
        start_vertex = self.get_vertex(start)
        end_vertex = self.get_vertex(end)
        if not start_vertex or not end_vertex:
            return None

        visited = set()
        parent = {}
        cycle = []
        
        def dfs(v, target):
            visited.add(v)
            for edge in self.outgoing[v].values():
                u = edge.opposite(v)
                if u not in visited:
                    parent[u] = v
                    if dfs(u, target):
                        return True
                elif u != parent.get(v) and (v == end_vertex or u == end_vertex):
                    cycle.append(u)
                    while v != u:
                        cycle.append(v)
                        v = parent[v]
                    cycle.append(u)
                    return True
            return False

        parent[start_vertex] = None  # Initialize the start vertex's parent
        if dfs(start_vertex, end_vertex):
            return cycle
        else:
            return None
        
    def visualize(self):
        nx_graph = self.to_networkx_graph()
        pos = nx.spring_layout(nx_graph, k=0.15, iterations=50)

        plt.figure(figsize=(12, 8))
        nx.draw(nx_graph, pos, with_labels=True, node_size=200, node_color='skyblue', font_size=6, font_weight='bold', edge_color='gray', width=1)

        plt.title("Graph Visualization", fontsize=14, fontweight='bold')
        plt.show()

    def to_networkx_graph(self):
        g = nx.Graph() if not self.is_directed() else nx.DiGraph()
        for vertex in self.vertices():
            g.add_node(vertex.userid, label=vertex.userid)
        for edge in self.edges():
            u, v = edge.endpoints()
            g.add_edge(u.userid, v.userid)
        return g
    
    #Returns Transitive edge
    #O(V)
    def transitive_follow(self,u):
        a1=[]
        for i in self.outgoing[u]:
            a1.append(self.outgoing[i])
        return a1
    

    def find_interest_vertex(self):
        vertices = self.vertices()
        interest_list1 = []
        interest_list2 = []
        interest_list3 = []
        for i in vertices:
            if i.interests == 'biking':
                interest_list1.append(i.userid)
            elif i.interests == 'sports':
                interest_list2.append(i.userid)
            elif i.interests == 'public speaking':
                interest_list3.append(i.userid)
        return interest_list1,interest_list2,interest_list3
   
    def create_random_graph(self, vertices):
        G = nx.Graph()
        G.add_nodes_from(vertices)
        for node in vertices:
            # Create random edges, excluding self-loops
            edges = []
            while len(edges) < random.randint(1, len(vertices) // 2):
                dest = random.choice(vertices)
                if dest != node and (node, dest) not in edges:
                    edges.append((node, dest))
            G.add_edges_from(edges)
        return G


    def visualize_graphs(self, G1, G2, G3):
        plt.figure(figsize=(15, 5))

        plt.subplot(131)
        nx.draw(G1, with_labels=True, node_color='lightblue', edge_color='gray', node_size=400, font_size=7)
        plt.title('Biking community')

        plt.subplot(132)
        nx.draw(G2, with_labels=True, node_color='lightgreen', edge_color='gray', node_size=400, font_size=7)
        plt.title('Sports community')

        plt.subplot(133)
        nx.draw(G3, with_labels=True, node_color='lightcoral', edge_color='gray', node_size=400, font_size=7)
        plt.title('Public speaking community')

        plt.show()

    def cluster(self):
        get_interest1,get_interest2,get_interest3 = self.find_interest_vertex()
        G1 = self.create_random_graph(get_interest1)
        G2 = self.create_random_graph(get_interest2)
        G3 = self.create_random_graph(get_interest3)
        self.visualize_graphs(G1, G2, G3)
    
# Function To do Depth First Search 
# O(V+E)
def DFS(g, u, discovered):
    for e in g.incident_edges(u.element):
        v = e.opposite(u)
        if v not in discovered:
            discovered[v] = e
            DFS(g,v,discovered)

# Function to know the path between Two vertex
# O(N)
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
# 
def test_connectivity(g,discovered):
    return len(discovered) == g.vertices_count()


