
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"({self.value}, {self.next})"

def remove_dup_recur(node, next_node):
    if node.value == next_node.value:
        node.next = next_node.next
        del next_node
        return node
    return node.next

def remove_dup(lst):
    # Fill this in.
    if lst is not None or lst.next is not None:
        node = lst
        next_node = lst.next
        while next_node:
            node = remove_dup_recur(node, next_node)
            next_node = node.next

def remove_dup_nosort(lst):
    if lst is not None or lst.next is not None:
        cycle = {}
        node = lst
        next_node = lst.next
        while next_node.next:
            if node.value == next_node.value or cycle.setdefault(node.value, None) is not None:
                node.next = next_node.next
                del next_node
                next_node = node.next
            else:
                cycle[node.value] = next_node.value
                node = next_node
                next_node = next_node.next
        print(cycle.setdefault(next_node.value, None))
        if cycle.setdefault(next_node.value, None) is not None:
            node.next = None

lst = Node(1, Node(2, Node(3, Node(2, Node(3)))))
remove_dup_nosort(lst)
print(lst)
# (1, (2, (3, None)))
