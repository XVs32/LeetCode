class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.Stack = []
        return

    def push(self, x: int) -> None:
        self.Stack.append(x)
        return

    def pop(self) -> None:
        self.Stack.pop()
        return

    def top(self) -> int:
        return self.Stack[-1]

    def getMin(self) -> int:
        return min(self.Stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()