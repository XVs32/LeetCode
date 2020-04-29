# day_03: Maximum Subarray

###### tags: `online_judge`, `python3`

求最大連續區間和。唯一需要注意的是，題目要求至少包含一個元素，也就是說最小值不一定為零。

記錄區間和，基於 greedy 在遇到區間和小於零的時候放棄當前區間和。

---

## 題目

```
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

---

## 解答

```python=
class Solution:
    def maxSubArray(self, nums):
        sums_previous = 0
        sums_now = 0
        max_sum = nums[0] 

        for i in range(len(nums)):
            sums_now = sums_previous + nums[i] 
            
            if max_sum < sums_now:
                max_sum = sums_now
            
            if sums_now < 0 :
                sums_now = 0
                
            sums_previous = sums_now
        return max_sum
        
        
a = Solution()
print (a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print (a.maxSubArray([1,2,3,4,5,6,7,8,9,10]))
print (a.maxSubArray([-1,-2,-3,-4,-5,-6]))
print (a.maxSubArray([-2,1]))
print (a.maxSubArray([-2,-1]))
```

---
### 成績

![](https://i.imgur.com/3ywJ64U.png)

---