# **Linked Lists**
In Python, a Linked List is similar to an array. It's a way to store a collection of information. However, unlike an array, a linked list stores its information randomly in memory. Each element in a linked list stores a piece of information randomly in memory, then also holds a reference pointing to the next item in the linked list.

## **Linked List Syntax**
A link list is comprized of nodes. Each node stores a value (our information) and a link to the next node in the list. This link will point to the next node's memory location so we can keep our list all together.

![Visualization of Linked List](images/linkedlist1.PNG)

In the visualization above, we can better see what makes up a linked list. The start of the linked list is known as the head. This is the start, or beginning of our list. It's similar to index zero in a dynamic array. We can also see our nodes, which contain our value and pointer to the next node.

This could be useful for navigating a list, but how can we go backwards? Once we move forward in the list we have nothing pointing us back to where we once were. We get stuck if we want to go backwards in this linked list.

**Doubly Linked Lists**

This is where doubly linked lsits come in. In addition to everythin a normal linked list has, they store a secondary pointer that points to the previous node. So instead of storing a value and one pointer, a doubly linked list will store a value and two pointers. One pointer will point to the next node, and the second will point to the previous node. 

![Visualization of Doubly Linked List](images/linkedlist2.PNG)

On a doubly linked list, we have a head and a tail. The head is the beginning or starting node in the list. The tail is the end node in the list. These endpoints help us keep track of our list.

---
## **Inserting Into a Linked List**
Inserting a new node into a linked list can be a bit more complicated. You have to add the new value, point to the previous and next values for the new node, and update the existing nodes you inserted the node next to.

**Inserting into the Head**

1. Create a new node
2. Set the "next" pointer of the new node to the current head
3. Set the "previous" pointer of the current head to the new node
4. Set the head equal to the new node

![Visualization of Inserting new Head in Linked List](images/linkedlist3.PNG)

**Inserting into the Tail**

1. Create a new node
2. Set the "previous" pointer of the new node to the current tail
3. Set the "next" pointer of the current tail to the new node
4. Set the tail equal to the new node

![Visualization of Inserting new Tail in Linked List](images/linkedlist4.PNG)

**Inserting into the Middle**

1. Create a new node
2. Set the "previous" pointer of the new node to the current node
3. Set the "next" pointer of the new node to the next node of the current node
4. Set the "previous" pointer of the "next" node after the current node to the new node
5. Set the next of the current node to the new node

![Visualization of Inserting into Middle of Linked List](images/linkedlist5.PNG)

**Practice**

That was a lot of information to digest. Let's go over what this might look like in code. First, let's code out how to insert into the head of a linked list. Let's imagine we have a class for LinkedList and a class for Node.
```python
import LinkedList
import Node

#Step 1: Create new node
new_node = LinkedList.Node(value)

# Step 2: Connect new node to the previous head
new_node.next = self.head
# Step 3: Connect the previous head to the new node 
self.head.prev = new_node
# Step 4: Update the head to point to the new node
self.head = new_node 
```
Wait, let's pause to think. What if we're inserting in an empty linked list? This code won't work for that. Let's examine how to handle that case.

```python
import LinkedList
import Node

#Step 1: Create new node
new_node = LinkedList.Node(value)

# If the list is empty, then point both head and tail
# to the new node.
if self.head is None:
    self.head = new_node
    self.tail = new_node

# If the list is not empty, then only self.head will be
# affected.
else:
    # Step 2: Connect new node to the previous head
    new_node.next = self.head
    # Step 3: Connect the previous head to the new node 
    self.head.prev = new_node
    # Step 4: Update the head to point to the new node
    self.head = new_node 
```

Take a moment to brainstorm how you might code out inserting a new node to the tail of a linked list. After thinking it through, go ahead and look at the next code example. Did you remember the handle the case of an empty Linked List?

```python
import LinkedList
import Node

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
```

Take a moment to think about how we might code inserting into the middle of a linked list. How would we handle the case of an empty linked list? Let's say we're inserting after a certain node.

```python
# Search for the node that matches 'value' by starting at the head of the list.
    curr = self.head
    while curr is not None:
        if curr.data == value:
            # If the location of 'value' is at the end of the list,
            # then we can call insert_tail to add 'new_value'
            if curr == self.tail:
                self.insert_tail(new_value)
            # For any other location of 'value', need to create a 
            # new node and reconenct the links to insert.
            else:
                # Step 1: Create a new node
                new_node = LinkedList.Node(new_value)
                # Step 2: Connect new node to the node containing 'value'
                new_node.prev = curr 
                # Step 3: Connect new node to the node after 'value'      
                new_node.next = curr.next
                # Step 4: Connect node after 'value' to the new node  
                curr.next.prev = new_node 
                # Step 5: Connect the node containing 'value' to the new node 
                curr.next = new_node       
                return # We can exit the function after we insert
            curr = curr.next # Go to the next node to search for 'value'
```

---
## **Removing From a Linked List**
Now let's go over the step to remove items from a linked list. Unlike the last section, we will combine the steps and the code syntax together. The example problem and practice problem at the end will help you if you are still struggling with the coding syntax.

The basic steps of removal are to delete the selected node, and update the next and previous nodes to point at eachother.

**Removing from Head**

1. Set the "previous" pointer of the second node to None (self.head.next.prev = None)
2. Set the second node to be the new head (self.head = self.head.next)
3. Delete the old head

![Visualization of Removing from Head of Linked List](images/linkedlist6.PNG)

**Removing from Tail**

---
## **Accessing From a Linked List**


---
## **Performance**


---
## **Example Problem:**


---
## **Problem to Solve:**
