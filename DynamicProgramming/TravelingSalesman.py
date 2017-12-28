import sys


class TravelingSalesman:
    def __init__(self):
        pass

    class Index:
        def __init__(self, current_vertex, set_of_vertices):
            self.current_vertex = current_vertex
            self.set_of_vertices = set_of_vertices

        def __hash__(self):
            value = self.current_vertex
            result = 17 * value + len(self.set_of_vertices) * 5
            return result

        def __eq__(self, other):
            if isinstance(other, type(self)) is not True:
                return False
            if other.current_vertex == self.current_vertex and set(other.set_of_vertices) == set(self.set_of_vertices):
                return True
            return False

    def calculate_cost(self, graph_array):
        minimum_cost_dictionary = {}
        parent_node_dictionary = {}
        all_possible_sets = self.generate_all_possible_sets(graph_array)

        for current_set in all_possible_sets:
            for current_vertex in range(1, len(graph_array)):
                if current_vertex in current_set:
                    continue

                index = self.Index(current_vertex, current_set)
                min_cost_value = sys.maxint
                min_previous_index = 0
                copy_set = set(current_set)

                for previous_vertex in current_set:
                    cost = graph_array[previous_vertex, current_vertex] + self.get_cost(copy_set, previous_vertex,
                                                                                        minimum_cost_dictionary)
                    if cost < min_cost_value:
                        min_cost_value = cost
                        min_previous_index = previous_vertex

                    if len(current_set == 0):
                        min_cost_value = graph_array[0, current_vertex]

                    minimum_cost_dictionary.update({index, min_cost_value})
                    parent_node_dictionary.update({index, min_previous_index})

        set_to_home = set()
        for i in range(1, len(graph_array)):
            set_to_home.add(i)
        min_value = sys.maxint
        prev_vertex = -1

        copy_set_to_home = set(set_to_home)
        for vertex in set_to_home:
            cost = graph_array[vertex, 0] + self.get_cost(copy_set_to_home, vertex, minimum_cost_dictionary)
            if cost < min_value:
                min_value = cost
                prev_vertex = vertex

        parent_node_dictionary.update({self.Index(0, set_to_home), prev_vertex})
        self.print_tour(parent_node_dictionary, len(graph_array))
        print(min_value)
        return min_value

    def get_cost(self, copy_set, prev_vertex, minimum_cost_dictionary):
        copy_set.remove(prev_vertex)
        index = self.Index(prev_vertex, copy_set)
        cost = 0
        if index in minimum_cost_dictionary:
            cost = minimum_cost_dictionary[index]
        copy_set.add(prev_vertex)
        return cost

    def print_tour(self, parent_node_dictionary, length):
        current_set = set()
        for i in range(0, length):
            current_set.add(i)
        start = 0
        stack = []

        while True:
            stack.append(start)
            current_set.remove(start)
            key = self.Index(start, current_set)
            if key in parent_node_dictionary:
                start = parent_node_dictionary[key]
            else:
                break

        output = ""
        for vertex in stack:
            output += vertex + "->"
        output = output[:-2]
        print(output)

    def generate_all_possible_sets(self, graph_array):
        input_array = []
        result_array = []
        for i in range(0, len(graph_array)):
            input_array[i] = i + 1
        all_sets = set()
        self.set_up_all_possible_sets(input_array, result_array, 0, 0, all_sets)
        all_sets = sorted(all_sets)
        return all_sets

    def set_up_all_possible_sets(self, input_array, result_array, start, pos, all_sets):
        if pos == len(input_array):
            return
        set_to_add = self.generate_set(result_array, pos)
        all_sets.add(set_to_add)
        for i in range(start, len(input_array)):
            result_array[pos] = input_array[i]
            self.set_up_all_possible_sets(input_array, result_array, start + 1, pos + 1, all_sets)

    @staticmethod
    def generate_set(result_array, pos):
        if pos == 0:
            return set()
        return_set = set()
        for i in range(0, pos):
            set.add(result_array[i])
        return return_set



