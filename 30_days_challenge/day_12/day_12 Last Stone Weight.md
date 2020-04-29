# day_12: Last Stone Weight

###### tags: `online_judge`, `python3`

給定一個非空的整數陣列，每次取出最大的兩個值相減，並把差值放回陣列，求陣列最後剩下的數字。

沒甚麼好說的，直接模擬整個過程。為了方便取得最大值，這邊使用 priority queue。

---

## 題目

```
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

    If x == y, both stones are totally destroyed;
    If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.

At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

 

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.

 

Note:

    1 <= stones.length <= 30
    1 <= stones[i] <= 1000
```

---

## 解答

```python=
from heapq import *

class Solution:
    def lastStoneWeight(self, stones):
        i = len(stones)
        
        j=0
        while j < i:
            stones[j] *= -1
            j+=1
            
        heapify(stones)

        while i > 1:
            a = heappop(stones)
            b = heappop(stones)
            
            if a != b:
                heappush(stones, a-b)
                i -= 1
            else:
                i -= 2
        
        if i == 0:
            return 0
        else:
            return -heappop(stones)

a = Solution()

print (a.lastStoneWeight([2,7,4,1,8,1]))
```

---
### 成績

![](https://i.imgur.com/QiPM3yg.png)


---