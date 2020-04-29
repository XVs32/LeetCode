class MinStack:
    
    a = []
    
    def __init__(self):
        self.a = []
        return None
        
    def push(self, x: int) -> None:
        self.a.append(x)
        return None

    def pop(self) -> None:
        self.a.pop()
        return None

    def top(self) -> int:
        return self.a[-1]

    def getMin(self) -> int:
        return min(self.a)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
        
