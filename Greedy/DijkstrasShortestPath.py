import sys

class DijkstrasShortestPath:
    vertex_count = 9  # Just setting the number of vertices here, in the real world you would calculate.

    def run(self, graph, start_vertex):
        dist = [None] * self.vertex_count  # set up the output array, dist[i] will hold short path from start to i
        shortest_path_set_for_items = [None] * self.vertex_count  # this will contain items with shortest path set

        for i in range(0, self.vertex_count):
            dist[i] = sys.maxint  # we begin by setting all distances from start as infinite
            shortest_path_set_for_items[i] = False  # we set all shortest path set vars to false

        dist[start_vertex] = 0  # distance from starting element to itself is always 0

        for count in range(0, self.vertex_count - 1):  # find shortest path for all vertices
            u = self._min_distance(dist, shortest_path_set_for_items)
            shortest_path_set_for_items[u] = True  # mark off the index, we found its shortest path
            for v in range(0, self.vertex_count):  # update the value of the adjacent vertices of the picked vertex
                if shortest_path_set_for_items is not True and graph[u][v] != 0 and dist[u] != sys.maxint \
                        and dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]

        self._print_solution(dist)

    def _min_distance(self, dist, shortest_path_set_for_items):  # function to find the min distance between vertices
        min_item = 0
        min_index = -1
        for v in range(0, self.vertex_count):
            if shortest_path_set_for_items[v] is False and dist[v] <= min_item:
                min_item = dist[v]
                min_index = v
        return min_index

    def _print_solution(self, dist):
        print "Distance from the vertex is "
        for i in range(self.vertex_count):
            print("{0} to {1}".format(i, dist[i]))
