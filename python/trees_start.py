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
        #Your code goes here
        pass
    

    def __contains__(self, data):
        return self._contains(data, self.root)  # Start at the root


    def _contains(self, data, node):
        #Your code goes here
        pass

    def __iter__(self):
        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):
        #Your code goes here
        pass
        
    def __reversed__(self):
        yield from self._traverse_backward(self.root)  # Start at the root

    def _traverse_backward(self, node):
        #Your code goes here
        pass



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



