
class Stack(object):
    def __init__(self):
        self.queue1 = []    # push
        self.queue2 = []    # pop

    def push(self, x):
        self.queue1.append(x)

    def pop(self):
        while len(self.queue1) > 1:
        	self.queue2.append(self.queue1.pop(0))
        res = self.queue1.pop(0)
        self.queue1, self.queue2 = self.queue2, self.queue1

    def top(self):
        return self.queue1[-1]
        
    def empty(self):                
        return not self.queue1[-1]

    def move(self):
        # move elements from stack 1 to stack 2
        # creates an actual stack
        # 1 2 3 4 5 --> 5 4 3 2 1
        while self.queue1:
            self.queue2.append(self.queue1.pop())


"""
        Pop
        push(x)
        1. Enqueue x into queue1
        pop()
        1. queue2 is initially empty, queue1 stores old elements:
            queue2 = []
            queue1 = [a, b, c, x]
        2. Dequeue each elements except the last one from queue1 to queue2:
            queue2 = [a, b, c]
            queue1 = [x]
        3. Dequeue the last element of queue1, and store it as x:
            x = x
            queue2 = [a, b, c]
            queue1 = []
        4. Swap queue1 and queue2:
            x = x
            queue1 = [a, b, c]
            queue2 = []
        5. Return x
        """