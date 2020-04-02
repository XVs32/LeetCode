# day_2: Happy Number

###### tags: `online_judge`, `python3`

給定一個整數陣列，重複把各位數字各自平方再相加。問結果會否收儉至1。

以hash table記錄各輪出現的數字，首次重複出現的數字若為1，則輸出True，否則輸出False。

---

## 題目

```
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
```

---

## 解答

```python=
class Solution:
    def isHappy(self,n):
        ans = 0
        record = {}
        while True:
            if not record.__contains__(n):
                record[n] = True
                while n != 0:
                    ans += (n % 10) * (n % 10)
                    n = (int)(n / 10)
                n = ans
                ans = 0
            else:
                if n == 1:
                    return True
                else:
                    return False

a = Solution()
print (a.isHappy(19))
print (a.isHappy(1))
print (a.isHappy(0))
```

---
### 成績

![](https://i.imgur.com/yHlmiUW.png)

---