# **Stacks: Last in First Out**

We use stacks all the time in Python. In the background, Python also uses stacks. I'm sure you've used stack tracing to debug your code.

A stack is a data structure in Python that describes the order in which items are added and removed. In a stack, the last item put into the list is the first item out.

---

## **Like Pancakes**

Imagine a stack of pancakes. As you make the pancakes, you stack them up on a plate. People come up and take the top, freshest pancake off the stack. This is essentially how stacks in Python work. If you make pancakes too quickly, the pancakes at the bottom will get cold because they are not being removed off the top.

### **Example**

Look at this code example. What numbers will be left?

```python
pancakes = []

pancakes.append(1)
pancakes.append(2)
pancakes.append(3)
pancakes.append(4)

pancakes.pop()
pancakes.pop()
```
So we create an empty array of pancakes. Then we add 1, 2, 3, and 4. Then we pop off the last two items, leaving us with 1 and 2.

```python
pancakes = []

pancakes.append(1) # 1
pancakes.append(2) # 1, 2
pancakes.append(3)  # 1, 2, 3
pancakes.append(4) # 1, 2, 3, 4

pancakes.pop() # 1, 2, 3
pancakes.pop() # 1, 2
```

---

## **The "Undo" Option**
Another good example of stacks is the "undo" option in a text editor. We've all pressed that back arrow or spammed "crtl + z" to undo the mistake (or mistakes) we have made.

Let's have a look at what happens when we type in a word document.

![Picture of word document](./images/OhNo.png)

Uh-oh! We have a typo. Let's press ctrl + z, or "pop" the item off the stack.

![Picture of word document](./images/One.png)

Let's do it again.. We need to get to our typo!

![Picture of word document](./images/Two.png)

Let's do it again.. We need to get to our typo!

![Picture of word document](./images/Three.png)

There we go. Now we need to "push" items back onto our stack. This time spelled correctly!

![Picture of word document](./images/Four.png)

### **Example**
What would our word document look like in python? Take a second to ponder this before looking at the code example below.
```python
sentence = []

sentence.append("This")
sentence.append("is")
sentence.append("me")
sentence.append("typing")
sentence.append("a")
sentence.append("sentence")
sentence.append("and")
sentence.append("I")
sentence.append("am")
sentence.append("bad")
sentence.append("at")
sentence.append("spelng")
sentence.append("it")
sentence.append("seems!")

sentence.pop() # removes "seems!"
sentence.pop() # removes "it"
sentence.pop() # removes "spelng"

sentence.append("spelling")
sentence.append("it")
sentence.append("seems!")
```

---

## **Operations**

![Table of common operations and big o](./images/table.png)


## Problem to Solve : Summer Camp Cost

Write a program utilizing your knowledge of stacks that will return the inverse of a given string.

You can test your program with the following string inputs:

* In: "racecar" 
    * Out: "racecar"
* In: "ham"
    * Out: "mah"
* In: "potatoes"
    * Out: "seotatop"
* In: "python"
    * Out: "nohtyp"

You can check your code with the solution here: [Solution](./python/invert_sentence.py)



[Back to Welcome Page](0-welcome.md)