class BST:

    class Node:

        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    def _insert(self, data, node):
        # If we already have this data, don't add it. Just return and end the loop.
        if data == node.data:
            return
        else:
            if data < node.data:
                # The data belongs on the left side.
                if node.left is None:
                    # We found an empty spot
                    node.left = BST.Node(data)
                else:
                    # Need to keep looking.  Call _insert
                    # recursively on the left sub-tree.
                    self._insert(data, node.left)
            else:
                # The data belongs on the right side.
                if node.right is None:
                    # We found an empty spot
                    node.right = BST.Node(data)
                else:
                    # Need to keep looking.  Call _insert
                    # recursively on the right sub-tree.
                    self._insert(data, node.right)
    

    def __contains__(self, data):
        return self._contains(data, self.root)  # Start at the root


    def _contains(self, data, node):
        if data == node.data:
            # If we have this info, return true!
            return True
        else:
            if data < node.data:
                # The data belongs on the left side.
                if node.left is None:
                    # We found an empty spot, so it doesn't exist here.
                    return False
                else:
                    # Need to keep looking.  Call _contains
                    # recursively on the left sub-tree to keep looking.
                    result = self._contains(data, node.left)
            else:
                # The data belongs on the right side.
                if node.right is None:
                    # We found an empty spot, so it doesn't exist here.
                    return False
                else:
                    # Need to keep looking.  Call _contains
                    # recursively on the right sub-tree to keep looking.
                    result = self._contains(data, node.right)
            return result

    def __iter__(self):
        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
        
    def __reversed__(self):
        yield from self._traverse_backward(self.root)  # Start at the root

    def _traverse_backward(self, node):
        if node is not None:
            # Go right first in order to reverse the order.
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)



print("\n=========== Insert & Forwards ===========")
tree = BST()
tree.insert(6)
tree.insert(3)
tree.insert(3)
tree.insert(6)  
tree.insert(7)
tree.insert(8)
tree.insert(4)
for x in tree:
    print(x)  # 3, 4, 6, 7, 8


print("\n=========== Reversed ===========")
for x in reversed(tree):
    print(x)  # 8, 7, 6, 4, 3



