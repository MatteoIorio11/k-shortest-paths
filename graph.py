class Vertex:
    def __init__(self, vertex: int):
        self.vertex = vertex
        self.neighboors = {}

    def getNeighboors(self):
        return self.neighboors
    
    def getVertex(self):
        return self.vertex
    
    def getCost(self, other: int):
        return self.neighboors.get(other, float('inf'))
    
    def addNeighboor(self, neigh, cost: int):
        if neigh not in self.neighboors:
            self.neighboors.setdefault(neigh, cost)
    
    def __eq__(self, other):
        return isinstance(other, Vertex) and self.vertex == other.getVertex()

    def __hash__(self):
        return hash((self.vertex))
    
    def __str__(self):
        return f"Vertex {self.vertex}"


class Graph:
    size = 0
    vertexs = {}
    def __init__(self):
        self.size = 0
    
    def addVertex(self, vertex: int):
        if vertex not in self.vertexs:
            v = Vertex(vertex)
            self.vertexs[vertex]=v
            self.size += 1
    
    def addArch(self, v1: int, v2: int, cost: int):
        if cost > 0:
            if v1 in self.vertexs:
                self.vertexs[v1].addNeighboor(Vertex(v2), cost)
                
    def getVertex(self, v: int):
        if v in self.vertexs:
            return self.vertexs[v]
        else:
            return None
    
    def getSize(self):
        return self.size

import heapq
import numpy as np

def Dijkstra(graph: Graph, start: int, destination: int):
    if graph.getVertex(start) == None or graph.getVertex(destination) == None:
        return []
    l_i = np.full(graph.getSize()+1, float('inf'))
    l_i[start] = 0
    Pred = np.full(graph.getSize()+1, -1)
    heap = []
    heapq.heapify(heap)
    heapq.heappush(heap, (0, start))
    curr_vertex = start
    while curr_vertex != destination and len(heap) > 0:
        cost, curr_vertex = heapq.heappop(heap)
        if curr_vertex != destination:
            for vertex_value, cost in graph.getVertex(curr_vertex).getNeighboors().items():
                distance = l_i[curr_vertex] + cost
                print(f"Neigh {vertex_value} Current {curr_vertex} Cost {cost}")
                if l_i[vertex_value.getVertex()] > distance:
                    l_i[vertex_value.getVertex()] = distance
                    heapq.heappush(heap, (l_i[vertex_value.getVertex()], vertex_value.getVertex()))
                    Pred[vertex_value.getVertex()] = curr_vertex
            
    print(Pred)
    
    def build_path():
        path = [destination]
        print(destination)
        curr_vertex = destination
        while curr_vertex != start:
            curr_vertex = Pred[curr_vertex]
            print(curr_vertex)
            path.append(curr_vertex)
        
        path.reverse()
        return path
        
        
    return build_path()


import csv

graph = Graph()


with open('graph.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        v1 = int(row[0])
        v2 = int(row[1])
        cost = int(row[2])
        graph.addVertex(v1)
        graph.addArch(v1, v2, cost)
        print(f"Node : Node1 {v1}, Graph Size: {graph.getSize()}")

print(graph.getSize())

print(Dijkstra(graph, 1, 4))

