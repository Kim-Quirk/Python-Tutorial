class Stack:
    def __init__(self):
        self.items = []
        self.size = 0

    def display(self):
        return print(self.items)

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def push(self, value):
        self.items.append(value)
        self.size += 1
        return str(value)

    def popOff(self):
        if self.isEmpty():
            return "Popping from an empty stack. Cannot complete task."
        remove = self.items[self.size - 1]
        self.items.pop()
        self.size -= 1
        return remove

# Here are the test cases. The comments indicate what the correct output is.
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