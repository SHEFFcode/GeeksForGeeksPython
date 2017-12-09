import sys

class DijkstrasShortestPath:
    vertex_count = 9  # Just setting the number of vertices here, in the real world you would calculate.

    def run(self, graph, start_vertex):
        min_dist = [sys.maxint] * self.vertex_count  # set up the output array, min_distance[i] will hold short path from start to i
        shortest_path_set_for_vertex = [False] * self.vertex_count  # this will contain items with shortest path set

        min_dist[start_vertex] = 0  # distance from starting element to itself is always 0

        for row in range(0, self.vertex_count - 1):  # find shortest path for all vertices, last one will not change the outcome
            min_distance_index = self._min_distance(min_dist, shortest_path_set_for_vertex)
            shortest_path_set_for_vertex[min_distance_index] = True  # mark off the index, we found its shortest path
            for column_vertex in range(0, self.vertex_count):  # update the value of the adjacent vertices of the picked vertex
                if shortest_path_set_for_vertex[column_vertex] is not True and graph[min_distance_index][column_vertex] != 0 and min_dist[min_distance_index] != sys.maxint \
                        and min_dist[min_distance_index] + graph[min_distance_index][column_vertex] < min_dist[column_vertex]:
                    min_dist[column_vertex] = min_dist[min_distance_index] + graph[min_distance_index][column_vertex]

        self._print_solution(min_dist)

    def _min_distance(self, dist, shortest_path_set_for_items):  # function to find the min distance between vertices
        min_item = sys.maxint
        min_index = -1
        for vertex in range(0, self.vertex_count):
            if shortest_path_set_for_items[vertex] is False and dist[vertex] <= min_item:
                min_item = dist[vertex]
                min_index = vertex
        return min_index

    def _print_solution(self, dist):
        print "Distance from the vertex is "
        for i in range(self.vertex_count):
            print("{0} to {1}".format(i, dist[i]))
