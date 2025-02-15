class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

    def to_string(self) -> str:
        if self.next is None:
            return f"{self.val}"
        return f"{self.val} -> {self.next.to_string()}"

    def print(self):
        print(self.to_string())

    def append(self, next: int):
        this_node = self
        while this_node.next is not None:
            this_node = this_node.next
        this_node.next = Node(next)

    def append_list(self, vals: list[int]):
        for v in vals:
            self.append(v)

    def reverse(self):
        prev, curr = None, self
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self = prev

# def reverse(node: Node) -> Node | None:
    # prev, curr = None, node
    # while curr:
    #     next = curr.next
    #     curr.next = prev
    #     prev = curr
    #     curr = next
    # return prev

node = Node(4)
node.append_list([5, 6, 7, 8, 9])
print("BEFORE REVERSING")
node.print()
node.reverse()
print("AFTER REVERSING")
node.print()
