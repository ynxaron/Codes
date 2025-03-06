class BinaryTree:
    # initializing a binary tree with the capibility to have no values, no left or right child
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None

    # the crux of printing algorithm is to use a queue such that we print the values of
    # current tree, then append to the right, if available, it's left child, if available it's
    # right child, and then pop this value that we have appended
    def to_string(self) -> str:
        return_string = ""
        tree_queue = [self] # beginning with the seed value
        while len(tree_queue) > 0: # while there is an element in our list to append / print
            new_tree_queue = [] # to replace this new queue since we are iterating over current vals
            this_str = ""
            for tree in tree_queue: # printing all the values
                this_str += str(tree.val) + " "
                if tree.left is not None and tree.left.val is not None: # then appending over our new list
                    new_tree_queue.append(tree.left)
                if tree.right is not None and tree.right.val is not None:
                    new_tree_queue.append(tree.right)
            return_string += this_str + "\n" # marking with a demarketer
            tree_queue = new_tree_queue
        return return_string

    def print(self):
        print(self.to_string())

    @staticmethod
    # the crux of the creating algorithm is to use a queue as well, iterating over the values
    # and appending to the right a left child and a right child
    def create(init: list[int]):
        return_tree = BinaryTree()
        tree_queue = [return_tree]
        for val in init:
            tree = tree_queue.pop(0)
            tree.val = val
            tree.left = BinaryTree()
            tree.right = BinaryTree()
            # this will work because at any time we would only have nodes in a single level,
            # and we would go a level down only after all nodes in the current level have been
            # exhausted
            tree_queue.append(tree.left)  # appending left
            tree_queue.append(tree.right) # appending right
        return return_tree

    # The crux of this algorithm is to use take the max height that came from left child, right child,
    # add 1 to that max and return that. Since the maximum depth node is either in left child or right child
    # this works, and since we have answer from one level lower, we must add 1 to the answer
    def height(self) -> int:
        leftHeight, rightHeight = 0, 0
        if self.left is not None and self.left.val is not None: # checking if 'left' node is valid
            leftHeight = self.left.height()
        if self.right is not None and self.right.val is not None: # checking if 'right' node is valid
            rightHeight = self.right.height()
        return max(leftHeight, rightHeight) + 1 # compensating since we searched from one depth lower
