
class Queue(object):
    def __init__(self):
        self.stack1 = []    # push
        self.stack2 = []    # pop

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        if not self.stack2:
            self.move()
        self.stack2.pop()

    def peek(self):
        if not self.stack2:
            self.move()
        return self.stack2[-1]
        
    def empty(self):                
        if not self.stack2:
            self.move()
        if not self.stack2:
            return True
        else:
            return False

    def move(self):
        # move elements from stack 1 to stack 2
        # creates an actual stack
        # 1 2 3 4 5 --> 5 4 3 2 1
        while self.stack1:
            self.stack2.append(self.stack1.pop())


"""
Implement the following operations of a queue using stacks.
push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:
* You must use only standard operations of a stack -- which means only push to
top, peek/pop from top, size, and is empty operations are valid.
* Depending on your language, stack may not be supported natively. You may
simulate a stack by using a list or deque (double-ended queue), as long as you
use only standard operations of a stack.
* You may assume that all operations are valid (for example, no pop or peek
operations will be called on an empty queue).
"""