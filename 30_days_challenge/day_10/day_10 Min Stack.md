# day_10: Min Stack

###### tags: `online_judge`, `python3`

完成 stack 的 push, pop, top, min 四種功能。
用 python 來寫基本沒有意義．．．各項功能都有內建。
push 可用 append
top 可用 stack[-1]

當然，也可以考慮自己實現一份來提高效率，但．．．
內建好了就用內建吧，除非對效能有很高要求（然而對效能有要求就不太應該選 python 了）

---

## 題目

```
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

 

Constraints:

    Methods pop, top and getMin operations will always be called on non-empty stacks.
```

---

## 解答

```python=
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
```

---
### 成績

![](https://i.imgur.com/48NEruw.png)

---