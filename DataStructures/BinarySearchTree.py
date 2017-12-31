class BinarySearchTree:
    class Node:
        def __init__(self, value=None):
            self.stored_value = value
            self.right_child = None
            self.left_child = None

    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value):
        if self.root is None:
            self.root = self.Node(value)
        else:
            self._find_and_insert(self.root, value)

    def _find_and_insert(self, current_node, value):
        if value > current_node.stored_value:
            if current_node.right_child is None:
                current_node.right_child = self.Node(value)
                self.size += 1
            else:
                self._find_and_insert(current_node.right_child, value)
        else:
            if value < current_node.stored_value:
                if current_node.left_child is None:
                    current_node.left_child = self.Node(value)
                    self.size += 1
                else:
                    self._find_and_insert(current_node.left_child, value)

    def search(self, target):
        return self._traverse(self.root, target)

    def _traverse(self, current_node, target):
        if current_node is None:
            return False;
        elif current_node.stored_value == target:
            return True
        if target > current_node.stored_value:
            self._traverse(current_node.right_child, target)
        else:
            self._traverse(current_node.left_child, target)
        return False

    def delete(self, delete_value):
        temp = []
        self._roundup(self.root, temp, delete_value)
        if len(temp) == self.size:
            print("Value {0} does not exist in the tree".format(delete_value))
        else:
            self.root = None
            self.size = 0
            to_insert = 0
            for i in range(0, len(temp)):
                to_insert = temp[i]
                self.insert(to_insert)
            print("Value {0} was deleted".format(delete_value))

    def _roundup(self, current_node, temp, delete_value):
        if current_node is None:
            return
        if current_node.stored_value != delete_value:
            temp.append(current_node.stored_value)
        self._roundup(current_node.left_child, temp, delete_value)
        self._roundup(current_node.right_child, temp, delete_value)
