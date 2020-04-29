# day_7: Counting Elements

###### tags: `online_judge`, `python3`

給定一個非空的整數陣列，問存在多少個 x，其中 x 和 x+1 同時是陣列的元素。

把陣列排序，並遍歷一次，遍歷時檢查下一個更大的元素是不是 x+1。



---

## 題目

```
Given an integer array arr, count element x such that x + 1 is also in arr.

If there're duplicates in arr, count them seperately.

 

Example 1:

Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.

Example 2:

Input: arr = [1,1,3,3,5,5,7,7]
Output: 0
Explanation: No numbers are counted, cause there's no 2, 4, 6, or 8 in arr.

Example 3:

Input: arr = [1,3,2,3,5,0]
Output: 3
Explanation: 0, 1 and 2 are counted cause 1, 2 and 3 are in arr.

Example 4:

Input: arr = [1,1,2,2]
Output: 2
Explanation: Two 1s are counted cause 2 is in arr.

 

Constraints:

    1 <= arr.length <= 1000
    0 <= arr[i] <= 1000

```

---

## 解答

```python=
class Solution:
    
    def countElements(self, arr):
        
        prev_num = None
        ans_counter = 0
        same_num_counter = 1
        
        for number in sorted(arr):
            
            if prev_num == number:
                same_num_counter += 1
                continue
                
            if prev_num == number - 1:
                ans_counter += same_num_counter
                
            prev_num = number
            same_num_counter = 1

        return ans_counter
        
a = Solution()

print (a.countElements([1,2,3]))
print (a.countElements([1,1,3,3,5,5,7,7]))
print (a.countElements([1,3,2,3,5,0]))
print (a.countElements([1,1,2,2]))
print (a.countElements([2,9,0,7,6,2,7,7,0]))
```

---
### 成績

![](https://i.imgur.com/nxdmfGg.png)

---