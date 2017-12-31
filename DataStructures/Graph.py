import LinkedList

class Graph:
    vertex_count = 0
    adjacency_list = []

    def __init__(self, vertex_count_input):
        self.vertex_count = vertex_count_input
        self.adjacency_list = [LinkedList.LinkedList() for x in range(0, self.vertex_count)]

    def add_edge(self, from_vertex, to_vertex):
        self.adjacency_list[from_vertex].add_node(to_vertex)
        self.adjacency_list[to_vertex].add_node(from_vertex)

    def remove_edge(self, from_vertex, to_vertex):
        self.adjacency_list[from_vertex].remove_node(to_vertex)
        self.adjacency_list[to_vertex].remove_node(from_vertex)


class GraphMatrix:
    vertex_count = 0
    adjacency_matrix = []

    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.adjacency_matrix = [[0 for x in range(0, vertex_count)] for x in range(0, self.vertex_count)]

    def add_edge(self, from_vertex, to_vertex):
        self.adjacency_matrix[from_vertex][to_vertex] = 1
        self.adjacency_matrix[to_vertex][from_vertex] = 1

    def remove_edge(self, from_vertex, to_vertex):
        self.adjacency_matrix[from_vertex][to_vertex] = 0
        self.adjacency_matrix[to_vertex][from_vertex] = 0