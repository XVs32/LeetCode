# day_5: Best Time to Buy and Sell Stock II

###### tags: `online_judge`, `python3`

給定一個整數陣列，順序找出各個區間最小、最大值之差的和。

就．．．遍歷的途中先找區間最小，再找區間最大就好了．．．

PS. ```0x7fffffff``` 是 32 位有號 int 的最大值。

---

## 題目

```
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.

Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

---

## 解答

```python=
class Solution:
    def maxProfit(self, prices):
        
        profit = 0
        lo = 0x7fffffff
        length = len(prices)
        
        i = 0
        while i < length:
            
            while i < length and lo > prices[i]:
                lo = prices[i]
                i += 1
                
            if i == length:
                break
                
            hi = prices[i]
            i += 1
            
            while i < length and hi < prices[i]:
                hi = prices[i]
                i += 1
                
            profit += hi - lo
            lo = 0x7fffffff
            
        if profit < 0:
            profit = 0
        
        return profit
        
a = Solution()
print (a.maxProfit([7,1,5,3,6,4]))
print (a.maxProfit([1,2,3,4,5]))
print (a.maxProfit([7,6,4,3,1]))
```

---
### 成績

![](https://i.imgur.com/MZ1XXDZ.png)

---