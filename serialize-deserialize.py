# coding: utf-8
class Tree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    def insert(self, key):
        def insert_rcs(node, key):
            if node is None:
                return Tree(key)
            elif node.key > key:
                node.left = insert_rcs(node.left, key)
            else:
                node.right = insert_rcs(node.right, key)
            return node
        self = insert_rcs(self, key)
    def __repr__(self):
        return '{} ('.format(self.key)
    
    def serialize_LNR(self):
        def serialize_rcs(node, result):
            if node is None:
                result.append('null')
                return
            else:
                result.append(node.key)
            serialize_rcs(node.left, result)
            serialize_rcs(node.right, result)
        result = []
        serialize_rcs(self, result)
        return result
    def serialize(self):
        queue = [self]
        result = []
        while queue:
            node = queue.pop(0)
            if node is None:
                result.append('null')
            else:
                result.append(node.key)
                queue.append(node.left)
                queue.append(node.right)
        result_str = '[' + ','.join(map(str, result)) + ']'
        return result_str
def deserialize(data):
    data = data[1:len(data)-1].split(',')
    data = list(map(lambda x: int(x) if x != 'null' else None, data))
    tree = Tree(data.pop(0))
    queue = [tree]
    while data:
        current_node = queue.pop(0)
        val = data.pop(0)
        if val is not None:
            current_node.left = Tree(val)
            queue.append(current_node.left)
        else:
            current_node.left = None
        
        val = data.pop(0)
        if val is not None:
            current_node.right = Tree(val)
            queue.append(current_node.right)
        else:
            current_node.right = None
    return tree
a = Tree(2);a.insert(3);a.insert(5);a.insert(1); a.insert(0); print(a.serialize())
b = deserialize(a.serialize()); print(b.serialize())
