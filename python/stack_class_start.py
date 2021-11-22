class Stack:
    def __init__(self):
        self.items = []
        self.size = 0

    def display(self):
        # Your code here..
        pass

    def getSize(self):
        # Your code here..
        pass

    def isEmpty(self):
        # Your code here..
        pass

    def push(self, value):
        # Your code here..
        pass

    def popOff(self):
        # Your code here..
        pass

# Here are your test cases. The comments indicate what the correct output is.
print("====== TEST CASES ======")

stack = Stack()
print("Added: " + stack.push("Pancake 1")) # Added: Pancake 1
print("Added: " + stack.push("Pancake 2")) # Added: Pancake 2
print("Added: " + stack.push(3)) # Added: 3
stack.display() # ['Pancake 1', 'Pancake 2', 3]
print("Size: " + str(stack.getSize())) # Size: 3
print("Removed: " + str(stack.popOff())) # Removed: 3
print("Size: " + str(stack.getSize())) # Size: 2
print("Is Empty: " + str(stack.isEmpty())) # Is Empty: False
print("Removed: " + str(stack.popOff())) # Removed: Pancake 2
print("Removed: " + str(stack.popOff()))# Removed: Pancake 1
print("Removed: " + str(stack.popOff())) # Removed: Popping from an empty stack. Cannot complete task.
print("Is Empty: " + str(stack.isEmpty())) # Is Empty: False