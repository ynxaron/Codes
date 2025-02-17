# We are defining a Node class, with several useful methods predefined
class Node:
    def __init__(self):
        self.val = None
        self.next = None

    # creating a Node class with mere list of ints
    @staticmethod
    def create(vals: list[int | None]):
        root = Node()
        root_clone = root
        for v in vals[:len(vals) - 1]: # we are using this because, at the last elem, it would
                                       # create last element point to a node with None in it's val
            root.val = v
            root.next = Node()
            root = root.next
        root.val = vals[len(vals) - 1] # then merely making the .val value of the last element make the last value
        return root_clone

    def to_string(self) -> str: # merely print this current value and then, if self.next is not None
        if self.next is None:
            return f"{self.val}"
        return f"{self.val} --> {self.next.to_string()}" # repeat this function for .next part

    def len(self) -> int: # merely increasing the len variable whenever a value is encountered
        len = 0
        while self is not None:
            self = self.next
            len += 1
        return len

    def to_list(self) -> list[int]: # appending the value to the vals list
        vals = []
        root = self
        while self is not None:
            vals.append(self.val)
            self = self.next
        self = root
        return vals

    def print(self):
        print(self.to_string())

    def to_num(self) -> int:
        ans = 0
        pow = 1
        while self is not None:
            ans += (pow * self.val)
            pow *= 10
            self = self.next
        return ans

    @staticmethod
    def from_num(init: int):
        root = Node()
        tail = root
        while init != 0:
            tail.val = (init % 10)
            init = init // 10
            if init != 0:
                tail.next = Node()
            tail = tail.next
        return root

    def remove_nones(self):
        root = self # creating a root variable so that head begins where None stops being prefixed
        while root.val is None: # if root.val is None, that is it has None there
            root = root.next
        tail = root
        while tail is not None:
            while tail.next is not None and tail.next.val is None: # if there is a next element, and that element is None, then skip that element
                tail.next = tail.next.next
            tail = tail.next
        return root
