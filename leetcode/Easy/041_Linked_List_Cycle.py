from Node_Lib import Node
def linked_list_cycle(n: Node) -> bool:
    slow, fast = n, n
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
