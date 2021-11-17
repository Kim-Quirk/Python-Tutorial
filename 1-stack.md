# Stacks

We use stacks all the time in Python. In the background, Python also uses stacks. I'm sure you've used stack tracing to debug your code.

A stack is a data structure in Python that describes the order in which items are added and removed. In a stack, the last item put into the list is the first item out.

## Like Pancakes: Last in First Out

Imagine a stack of pancakes. As you make the pancakes, you stack them up on a plate. People come up and take the top, freshest pancake off the stack. This is essentially how stacks in Python work. If you make pancakes too quickly, the pancakes at the bottom will get cold because they are not being removed off the top.

### **Example**

Look at this code example. What numbers will be left?

```python
pancakes = []

pancakes.push(1)
pancakes.push(2)
pancakes.push(3)
pancakes.push(4)

pancakes.pop()
pancakes.pop()
```
So we create an empty array of pancakes. Then we add 1, 2, 3, and 4. Then we pop off the last two items, leaving us with 1 and 2.

```python
pancakes = []

pancakes.push(1) # 1
pancakes.push(2) # 1, 2
pancakes.push(3)  # 1, 2, 3
pancakes.push(4) # 1, 2, 3, 4

pancakes.pop() # 1, 2, 3
pancakes.pop() # 1, 2
```

## The "Undo" Option
## Performance