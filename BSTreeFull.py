class Node:
    def __init__(self, key):
       self.key = key
       self.left = None
       self.right = None
    def insert(self, key):
       def insertRcs(node, key):
           if node is None:
               return Node(key)
           elif node.key < key:
               node.right = insertRcs(node.right, key)
           else:
               node.left = insertRcs(node.left, key)
           return node
       self = insertRcs(self, key)
