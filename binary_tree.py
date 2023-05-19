from node import Node


class BinaryTree:
    def __init__(self, head: Node):
        self.head = head

    def add(self, new_node: Node):
        current_node = self.head

        while current_node:
            if new_node.value == current_node.value:
                raise ValueError('A node with this value exists. No identical numbers allowed.')

            elif new_node.value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    break

            elif new_node.value > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    break

    def find(self, value: int):
        current_node = self.head

        while current_node:
            if value == current_node.value:
                return current_node
            elif value > current_node.value:
                current_node = current_node.right
            else:
                current_node = current_node.left
        raise ValueError(f'Value of {value} is not in this tree')

    def inorder(self):
        self._inorder_recursive(self.head)

    def _inorder_recursive(self, curr_node):
        if not curr_node:
            return
        self._inorder_recursive(curr_node.left)
        print(curr_node)
        self._inorder_recursive(curr_node.right)

    def preorder(self):
        self._preorder_recursive(self.head)

    def _preorder_recursive(self, curr_node):
        if not curr_node:
            return
        print(curr_node)
        self._inorder_recursive(curr_node.left)
        self._inorder_recursive(curr_node.right)

    def find_parent(self, value: int) -> Node:
        if self.head and self.head.value == value:
            return self.head

        current_node = self.head
        while current_node:
            if (current_node.left and current_node.left.value == value) or \
                    (current_node.right and current_node.right.value == value):
                return current_node
            elif value > current_node.value:
                current_node = current_node.right
            elif value < current_node.value:
                current_node = current_node.left

    @staticmethod
    def find_rightmost(self, node: Node) -> Node:
        current_node = node
        while current_node.right:
            current_node = current_node.right
        return current_node

    def delete(self, value: int):
        to_delete = self.find(value)
        to_delete_parent = self.find_parent(value)

        if to_delete.left and to_delete.right:
            rightmost = self.find_rightmost(to_delete.left)
            rightmost_parent = self.find_parent(rightmost.value)

            if to_delete == to_delete_parent.left:
                rightmost.right = to_delete.right
                to_delete_parent.left = rightmost

            if to_delete == to_delete_parent.right:
                rightmost_parent.right = rightmost.left
                rightmost.left = to_delete.left
                rightmost.right = to_delete.right
                to_delete_parent.right = rightmost

            else:
                rightmost.right = to_delete.right
                self.head = rightmost

        elif to_delete.left or to_delete.right:
            if to_delete == to_delete_parent.left:
                to_delete_parent.left = to_delete.left or to_delete.right
            elif to_delete == to_delete_parent.right:
                to_delete_parent.right = to_delete.left or to_delete.right
            else:
                self.head = to_delete.left or to_delete.right

        else:
            if to_delete == to_delete_parent.left:
                to_delete_parent.left = None
            elif to_delete == to_delete_parent.right:
                to_delete_parent.right = None
            else:
                self.head = None
