from node import Node
from binary_tree import BinaryTree

tree = BinaryTree(Node(9))
tree.add(Node(5))
tree.add(Node(11))

tree.inorder()
print('---')
tree.preorder()
print('---')
print(tree.find(11))
print(tree.find(13))
