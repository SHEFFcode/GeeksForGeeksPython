class LinkedList:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next_node = None

    def __init__(self):
        self.head_node = self.Node()
        self.tail_node = self.head_node

    def add_node(self, data):
        if self.head_node.data is None:
            self.head_node.data = data
        else:
            node_to_insert = self.Node(data)
            self.tail_node.next_node = node_to_insert
            self.tail_node = node_to_insert

    def remove_node(self, value):
        current_node = self.head_node
        previous_node = None
        while True:
            if current_node.data == value:
                if previous_node is None:  # we are at the head node
                    self.head_node = self.head_node.next_node  # just update the head node
                    self.tail_node = self.head_node
                    break
                else:
                    previous_node.next_node = current_node.next_node
                    if previous_node.next_node is None:
                        self.tail_node = previous_node
                    break
            else:
                previous_node = current_node
                current_node = current_node.next_node
            if current_node is None:
                break

    def traverse_linked_list(self):
        current_node = self.head_node
        while True:
            if current_node.data is None:
                break
            else:
                print(current_node.data)
                current_node = current_node.next_node
            if current_node is None:
                break
