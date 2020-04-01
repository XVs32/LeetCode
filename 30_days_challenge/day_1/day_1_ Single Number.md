# day_1: Single Number

###### tags: `online_judge`, `python3`

給定一個非空的整數陣列，其中除了一個特別的元素只會出現一次之外，所有元素皆會出現兩次。問該特別元素的值。

一般來說可以使用 hash table 來解，記錄各個 key (元素)的出現次數。

但同時在偶然在網路上發現了一個 bit-wise 解法。把各個元素轉換成 2 進制並記錄各位數 1 的出現次數。
例如給定```[4,4,1]```，
轉換為 2 進制後即為```[0b0100,0b0100,0b0001]```
各位數 1 的出現次數為```[0],[2],[0],[1]```
因為非特別的元素必定出現兩次，所以各位數的出現次數必為 2 的倍數。
因此對各個位數的記錄取 2 的餘數，即可去除所有非特別元素的記錄。
```[0 % 2],[2 % 2],[0 % 2],[1 % 2]``` -> ```[0],[0],[0],[1]```
將該筆二進制資料恢復為十進制即為解答。
```[0],[0],[0],[1]``` -> ```[0b0001]``` -> ```[1]```



---

## 題目

```
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1

Example 2:

Input: [4,1,2,1,2]
Output: 4
```

---

## 解答

python hash table version:
```python=
class Solution:

    def singleNumber(self, nums):
        
        table = {}
        
        for i in range(len(nums)):
            
            if not table.__contains__(nums[i]):
                table[nums[i]] = 1;
            else:
                table.pop(nums[i])
    
        return list(table)[0]
    
        
        
a = Solution()
print("%s" % a.singleNumber([2,2,1]))
print("%s" % a.singleNumber([4,1,2,1,2]))
print("%s" % a.singleNumber([4,1,2,1,2]))
```

C bitwise version:
```c=
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int singleNumber(int* nums, int numsSize){
    
    int i, j;
    unsigned int bit_map[32] = {0};
    
    for (i=0;i<numsSize;i++){
        for (j=0;j<32;j++){
            bit_map[j] += (nums[i] >> j & 1);
        }
    }
    
    int ans=0;
    for (j=0;j<32;j++){
        ans += (bit_map[j] % 2 << j);
    }
    
    return ans;
}

int main(){
    
    int num0[] = {2,2,1};
    printf("%d\n",singleNumber(num0,3));
    
    int num1[] = {4,1,2,1,2};
    printf("%d\n",singleNumber(num1,5));
    
    int num2[] = {-1};
    printf("%d\n",singleNumber(num2,1));
    
}
```

---
### 成績

![](https://i.imgur.com/nGfRpAr.png)
![](https://i.imgur.com/wZnFigd.png)


---