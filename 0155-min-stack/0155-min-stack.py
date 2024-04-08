class MinStack:

    def __init__(self):
       self.stacks = []

        

    def push(self, val: int) -> None:
        if len(self.stacks) == 0:
            self.stacks.append([val,val])
        else:
            top_elt = self.stacks[-1]
            if top_elt[1] < val:
              
                self.stacks.append([val,top_elt[1]])
            else:
                self.stacks.append([val,val])
                

    def pop(self) -> None:
        self.stacks.pop()
         

        

    def top(self) -> int:
        return self.stacks[-1][0]
    

    def getMin(self) -> int:
        top_elt = self.stacks[-1]
        return top_elt[1]
        
              

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()