class LinkedList:

    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_head(self, value):
        # Create the new node
        new_node = LinkedList.Node(value)  
        
        # If the list is empty, then point both head and tail
        # to the new node.
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # If the list is not empty, then only self.head will be
        # affected.
        else:
            new_node.next = self.head # Connect new node to the previous head
            self.head.prev = new_node # Connect the previous head to the new node
            self.head = new_node      # Update the head to point to the new node

    def insert_tail(self, value):
        # Create the new node
        new_node = LinkedList.Node(value)  
        
        # If the list is empty, then point both head and tail
        # to the new node.
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # If the list is not empty, then only self.tail will be
        # affected.
        else:
           new_node.prev = self.tail
           self.tail.next = new_node
           self.tail = new_node
    
    def __iter__(self):
        """
        Iterate foward through the Linked List
        """
        curr = self.head  # Start at the begining since this is a forward iteration.
        while curr is not None:
            yield curr.data  # Provide (yield) each item to the user
            curr = curr.next # Go forward in the linked list
    
    def __str__(self):
        """
        Return a string representation of the linked list.
        """
        output = "linkedlist["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output
    
    def add_values(self, position1, position2):
        # Initilize your variables
        count1 = 1
        count2 = 1
        node_one = self.head #We need to loop through twice, so lets have two nodes made
        node_two = self.head

        #While our count is not the position we want, keep going...
        while count1 is not position1:
            node_one = node_one.next #Move to next node
            count1 += 1 #increment our count
        value1 = node_one.data #Our count is equal to our position now. So let's store this node's value!

        #Repeat the same process, with different variables to avoid confusion
        while count2 is not position2:
            node_two = node_two.next
            count2 += 1
        value2 = node_two.data

        return value1 + value2 #Return the result
            

ll = LinkedList()
ll.insert_tail(1)
ll.insert_head(6)
ll.insert_head(2)
ll.insert_head(7)
ll.insert_head(3)
ll.insert_head(4)
ll.insert_head(5)
print(ll)
print(ll.add_values(1, 3)) #8
print(ll.add_values(3, 5)) #5
print(ll.add_values(2, 4)) #11
print(ll.add_values(5, 6)) #8

