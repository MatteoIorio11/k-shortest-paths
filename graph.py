class Vertex:
    def __init__(self, vertex: int):
        self.vertex = vertex
        self.neighbors = {}

    def getneighbors(self):
        return self.neighbors
    
    def getVertex(self):
        return self.vertex
    
    def getCost(self, other: int):
        return self.neighbors.get(other, float('inf'))
    
    def addneighbor(self, neigh, cost: int):
        if neigh not in self.neighbors:
            self.neighbors.setdefault(neigh, cost)
    
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
        self.vertexs = {}
    
    def addVertex(self, vertex: int):
        if vertex not in self.vertexs:
            v = Vertex(vertex)
            self.vertexs[vertex]=v
            self.size += 1
    
    def addArch(self, v1: int, v2: int, cost: int):
        if cost > 0:
            if v1 not in self.vertexs:
                self.addVertex(v1)
            self.vertexs[v1].addneighbor(Vertex(v2), cost)
                
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
    """_summary_

    Args:
        graph (Graph): Graph, where all the vertex are stored
        start (int): starting vertex
        destination (int): destination vertex

    Returns:
        list : path from start to destination
    """
    if graph.getVertex(start) == None or graph.getVertex(destination) == None:
        return []
    l_i = np.full(graph.getSize()+1, float('inf'))
    Pred = np.full(graph.getSize()+1, -1)
    heap = []
    l_i[start] = 0
    heapq.heapify(heap)
    heapq.heappush(heap, (0, start))
    curr_vertex = start
    while curr_vertex != destination and len(heap) > 0:
        cost, curr_vertex = heapq.heappop(heap)
        if curr_vertex != destination:
            for vertex_value, cost in graph.getVertex(curr_vertex).getneighbors().items():
                distance = l_i[curr_vertex] + cost
                if l_i[vertex_value.getVertex()] > distance:
                    l_i[vertex_value.getVertex()] = distance
                    heapq.heappush(heap, (l_i[vertex_value.getVertex()], vertex_value.getVertex()))
                    Pred[vertex_value.getVertex()] = curr_vertex
        
    def build_path():
        path = [destination]
        curr_vertex = destination
        while curr_vertex != start:
            curr_vertex = Pred[curr_vertex]
            path.append(curr_vertex)
        
        path.reverse()
        return path
        
    return build_path()


def K_Dijkstra(graph: Graph, start: int, destination: int, k: int):
    """_summary_

    Args:
        graph (Graph): Graph, where all the vertex are stored
        start (int): starting Vertex
        destination (int): destination Vertex
        k (int): how many paths must be generated

    Returns:
        list(list): where all the k-paths are stored from start to destination 
    """
    paths = []
    heap = [(0, [], start)]
    while heap and len(paths) < k:
        cost, path, current_node = heapq.heappop(heap)
        path = path + [current_node]
        if current_node and current_node == destination:
            paths.append(path)
        elif graph.getVertex(current_node):
            for neighbor, weight in graph.getVertex(current_node).getneighbors().items():
                if neighbor.getVertex() not in path:
                    heapq.heappush(heap, (cost + weight, path, neighbor.getVertex()))

    return paths


