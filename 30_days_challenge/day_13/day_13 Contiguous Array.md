# day_13: Contiguous Array

###### tags: `online_judge`, `python3`

給定一個只有 0 和 1 的陣列，求 0 和 1 數量相等的最大子陣列。

又是一題 hash table（好啦，其實是前綴和），求各前綴的 0,1 數量差，若有兩個前綴帶有相同 0,1 數量差，則這兩個前綴相減結果會是一個 0 和 1 數量相等的子陣列。
而 hash table 可用於記錄各數量 0,1 的對應前綴。
順帶一提，因為是要找最大子陣列，hash table 只要記錄每個 0,1 數量差最早找到的前綴就可以了（越後期找到的，距離肯定越短啊）。

---

## 題目

```
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:

Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:

Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000. 
```

---

## 解答

```python=
class Solution:
    def findMaxLength(self, nums):
        
        prefix_sum = {}
        prefix_sum[0] = -1
        diff = 0
        ans = 0
        
        for i in range(len(nums)):
            if(nums[i]==0):
                diff-=1
            else:
                diff+=1
            
            if diff in prefix_sum:
                ans = max(i - prefix_sum[diff],ans)
            else:
                prefix_sum[diff] = i
            
        return ans
    
a = Solution()

print (a.findMaxLength([0,1]))
print (a.findMaxLength([0,1,0]))
print (a.findMaxLength([]))
print (a.findMaxLength([0,0,0,0]))
print (a.findMaxLength([0,1,1,1,1,0,0]))
```

---
### 成績

![](https://i.imgur.com/DIAd7Wo.png)

---