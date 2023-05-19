from node import Node
from binary_tree import BinaryTree

tree = BinaryTree(Node(6))

nodes = [5, 2, 9, 7, 8, 9.5, 12, 42, 33]

for num in nodes:
    tree.add(Node(num))

tree.delete(9)
print(tree.inorder())
