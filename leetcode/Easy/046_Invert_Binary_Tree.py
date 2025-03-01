from BTree_Lib import BinaryTree
# We are inverting a binary tree by simply first inverting the left child, the right child,
# then placing the left child at right child's place and right child at left child's place
def invert_tree(tree: BinaryTree):
    if tree.left is not None: # making sure there is a left child
        invert_tree(tree.left)
    if tree.right is not None: # making sure there is a right child
        invert_tree(tree.right)
    if tree.left is not None and tree.right is not None: # now inverting the parents
        left = tree.left
        tree.left = tree.right
        tree.right = left

tree = BinaryTree.create([1, 2, 3, 4, 5, 6])
tree.print()
invert_tree(tree)
tree.print()
