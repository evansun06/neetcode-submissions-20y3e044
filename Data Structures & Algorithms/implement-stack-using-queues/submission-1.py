from collections import deque

class MyStack:
    """
    push(1), push(2), pop(), push(3), top(), pop()
    null.  , null   , 2.   , null.  , 3.   , 3
    q1 = 1, 2, 3

    """

    def __init__(self):
        self.queue = deque()
        self.top_val = None
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.top_val = x
        

    def pop(self) -> int:
        self.top_val = None
        size = len(self.queue)
        for i in range(size - 1):

            val = self.queue.popleft()

            if i == size - 2:
                self.top_val = val

            self.queue.append(val)
        
        return self.queue.popleft()

    
    def top(self) -> int:
        return self.top_val
        

    def empty(self) -> bool:
        return True if len(self.queue) == 0 else False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
