# day_04:Move Zeroes

###### tags: `online_judge`, `python3`

給定一個整數陣列，把陣列中所有的零移至陣列最後，並且不能影響到其他元素的順序。

這題可以使用快慢指標，一個快指標指向讀取到的位置，另一個慢指標指向寫入到的位置。快慢指標在每輪寫入非零值後加一，快指標在讀取到零值時也加一，當快指標指向陣列末尾時，慢指標後方所有元素皆更改為一。

---

## 題目

```
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:

    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.
```

---

## 解答

```python=
class Solution:
    def moveZeroes(self, nums):
        
        fast_id = 0
        slow_id = 0
        length = len(nums)
        
        while slow_id + fast_id < length:
            
            if nums[slow_id + fast_id] == 0:
                fast_id += 1
                continue
                
            nums[slow_id] = nums[slow_id + fast_id]
            slow_id += 1
            
        while slow_id < length:
            nums[slow_id] = 0
            slow_id += 1
        
        return nums
        
a = Solution()
print (a.moveZeroes([0,1,0,3,12]))
print (a.moveZeroes([0,0,1]))
print (a.moveZeroes([0,1,0]))
print (a.moveZeroes([1,0,0]))
print (a.moveZeroes([-2,-1]))
```

---
### 成績

![](https://i.imgur.com/WRsa5M3.png)

---