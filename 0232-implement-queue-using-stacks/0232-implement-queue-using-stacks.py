class MyQueue:

    def __init__(self):
        self.stack = []
        self. tomake_queue = []
        

    def push(self, x: int) -> None:
        while self.stack:
            elt = self.stack.pop()
            self.tomake_queue.append(elt)
        self.stack.append(x)
        while self.tomake_queue:
            elt = self.tomake_queue.pop()
            self.stack.append(elt)
            
            
        

    def pop(self) -> int:
        return self.stack.pop()
        

    def peek(self) -> int:
        return self.stack[-1]
        

    def empty(self) -> bool:
        return not len(self.stack)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()