import random
AVG_ARR_LEN: int = 15
ARR_LIMIT: int = 40
class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

    def maxVal(self) -> int:
        while self.right is not None:
            self = self.right
        return self.val

    def minVal(self) -> int:
        while self.left is not None:
            self = self.left
        return self.val

    def push(self, n: int):
        while (self.left is not None) or (self.right is not None):
            if self.val > n:
                if self.left is not None:
                    self = self.left
                    continue
                break
            if self.val < n:
                if self.right is not None:
                    self = self.right
                    continue
                break

        if self.val < n:
            self.right = Node(n)
        if self.val > n:
            self.left = Node(n)

array = []
for _ in range(AVG_ARR_LEN):
    val = random.randint(1, ARR_LIMIT)
    while val in array:
        val = random.randint(1, ARR_LIMIT)
    array.append(val)

#array = [31, 16, 14, 5, 24, 8, 35, 2, 40, 18, 33, 22, 36, 25, 11]
array = [6, 3, 8, 5, 2, 1, 9]
print(array)
node = Node(array[0])
for n in array[1:]:
    node.push(n)
