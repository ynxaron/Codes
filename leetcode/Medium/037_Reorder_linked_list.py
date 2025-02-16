class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

    @staticmethod
    def create(vals: list[int]):
        root = Node(vals[0])
        tail = root
        for v in vals[1:]:
            tail.next = Node(v)
            tail = tail.next
        return root

def reorder_linked_list(node: Node) -> Node:
    root = node
    # BUG: Implement the algorithm here
    return root
