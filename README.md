# LeetCode record

[TOC]

## 219_easy
超越 easy 難度的 easy 題目。網路上充斥著暴力解法，但那是會吃到 TLE 的。加上沒有給出 input 的數值範圍，都讓本題的難度上升不少。

正確方案是使用hash table。以 hash 過的 ```nums``` 為 key，並在 slot 上記錄該 ```nums``` 的 index。

python 的話可以使用 dict 簡單的達到要求，如果寫 C 的話... 就自（自）求（己）多（去）福（刻）吧。

```
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false


```

```python3=
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        
        table = {}
        
        for i in range(len(nums)):
            
            if not table.__contains__(str(nums[i])):
                table[str(nums[i])] = i;
            elif i - table[str(nums[i])] <= k:
                return True
            else :
                table[str(nums[i])] = i;

        return False
	
a = Solution()
print (a.containsNearbyDuplicate([1,2,3,1],3))
print (a.containsNearbyDuplicate([1,0,1,1],1))
print (a.containsNearbyDuplicate([1,2,3,1,2,3],2))
print (a.containsNearbyDuplicate([1,2,3],0))
```


## 