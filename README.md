# LeetCode record

[TOC]

## 219. Contains Duplicate II (easy)
超越 easy 難度的 easy 題目。網路上充斥著暴力解法，但那是會吃到 TLE 的。加上沒有給出 input 的數值範圍，都讓本題的難度上升不少。

正確方案是使用hash table。以 hash 過的 ```nums``` 為 key，並在 slot 上記錄該 ```nums``` 的 index。

python 的話可以使用 dict 簡單的達到要求，如果寫 C 的話... 就自（自）求（己）多（去）福（刻）吧。

---
題目：
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
---
解答：

```python=
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


## 784. Letter Case Permutation (easy)

熱身 easy 題目。各個字母都有大、小寫兩種可能。以 recursive 展開即可，以本題的複雜度來說，改用迴圈也不是不行。只是...我懶。

---
題目：
```
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]

Note:

    S will be a string with length between 1 and 12.
    S will consist only of letters or digits.
```


---
解答：

```python=
class Solution:
    
    ans = []
    
    def letterCasePermutation(self, S: str) -> List[str]:
        self.ans = []
        self.dfs(S,0)
        return self.ans
        
    def dfs(self, input,start_index) -> List[str]:
        
        for i in range(start_index,len(input)):
            if input[i].isalpha():
                
                input = input[:i] + input[i].lower() + input[i+1:]
                self.dfs(input,i+1)

                input = input[:i] + input[i].upper() + input[i+1:]
                self.dfs(input,i+1)

                return
                
        self.ans.append(input)
        return
```


## 842. Split Array into Fibonacci Sequence (medium)

隱藏地雷的 medium 題。使用暴力列舉前兩個數字的所有長度可能性即可，考量至少須要 3 個數字組成，可以多少縮減長度範圍。

需要注意 3 點：

1. 第 2 個數字長度可以比第 1 個數字短，這跟 Fibonacci Sequence 不一樣。
2. 不容許以零為首的數字，例如```02```。單一個零，即```0```則例外。
3. ***數列中所有數字範圍都必須在 32-bit int 內。***

第三點完全可能坑死 python 用家...　寫 C 的話倒大概是不會被坑到，LOL。


---
題目：
```
Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:

    0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
    F.length >= 3;
    and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.

Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.

Example 1:

Input: "123456579"
Output: [123,456,579]

Example 2:

Input: "11235813"
Output: [1,1,2,3,5,8,13]

Example 3:

Input: "112358130"
Output: []
Explanation: The task is impossible.

Example 4:

Input: "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.

Example 5:

Input: "1101111"
Output: [110, 1, 111]
Explanation: The output [11, 0, 11, 11] would also be accepted.

Note:

    1 <= S.length <= 200
    S contains only digits.

```



---
解答：
```python=
class Solution:
    
    def is_lead_zero(self,S):
        if len(S)>1 and S[0]=='0':
            return True
        else:
            return False
		
    def is_fib(self,S,fount,back):
        
        output = []
        output.append(fount)
        output.append(back)
        ans = str(int(fount) + int(back))
        
        start = len(fount) + len(back)
        end = start + len(ans)
        
        if S[start:end] != ans or int(ans)>2147483647:
            output = []
            return output
        
        output.append(ans)
        
        while end<len(S):
            fount = back
            back = ans
            ans = str(int(fount) + int(back))

            start = end
            end = start + len(ans)

            if S[start:end] != ans or int(ans)>2147483647:
                output = []

                return output
            output.append(ans)
        return output
            
    
    def splitIntoFibonacci(self, S: str):
        
        
        for i in range(1,int(len(S))):
            fount = S[0:i]
            if self.is_lead_zero(fount) == True:
                continue
				
            for j in range(1,int(len(S))):
                if i + j > int(len(S)/3)*2+1:
                    continue
                output = []

				
                back = S[i:i+j]
                if self.is_lead_zero(back) == True:
                    continue
                
                output = self.is_fib(S,fount,back)
                if output:
                    return output
		
        empty = []
        return empty
        
a = Solution()
print (a.splitIntoFibonacci("0123"))
```

## 980. Unique Paths III (hard)

地圖尋路題，單純的 DFS 尋路即可解開。在開始尋路前記錄```0```的數量。在遞迴過程中以遞迴深度作為是否走過所有```0```的判斷。注意離開該次遞迴時必須把走過該點的標記恢復（本題走過即標記為```-1```）。

小技巧：
地圖題很多時候可以在邊緣圍上一層不可進入的標記，以省去處理邊緣問題的時間。

例如：
```
1  0  0
0 -1  0
0  0  2

```
可修改為：
```
-1 -1 -1 -1 -1
-1  1  0  0 -1
-1  0 -1  0 -1
-1  0  0  2 -1
-1 -1 -1 -1 -1
```

這樣就可以在整個尋路過程中使用同一套邏輯了。

---

題目：

```
On a 2-dimensional grid, there are 4 types of squares:

    1 represents the starting square.  There is exactly one starting square.
    2 represents the ending square.  There is exactly one ending square.
    0 represents empty squares we can walk over.
    -1 represents obstacles that we cannot walk over.

Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 

Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

Example 2:

Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

Example 3:

Input: [[0,1],[2,0]]
Output: 0
Explanation: 
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.

 

Note:

    1 <= grid.length * grid[0].length <= 20

```

---

解答：
```python=
class Solution:
    
    zero_count = 0
    max_x = 0
    max_y = 0
    path_count = 0
    
    def get_info(self, grid):
        s_x = -1
        s_y = -1
        zero_count = 0
        
        for i in range(self.max_y):
            for j in range(self.max_x):
                if grid[i][j] == 0:
                    zero_count += 1
                elif grid[i][j] == 1:
                    s_x = j
                    s_y = i
        return s_x,s_y,zero_count
        
    def find_path(self, grid, x, y, count):
        
        grid[y][x] = -1
        
        if grid[y][x+1] == 0:
            self.find_path(grid,x+1,y,count+1)
        elif grid[y][x+1] == 2 and count == self.zero_count:
            self.path_count += 1
            
        if grid[y][x-1] == 0:
            self.find_path(grid,x-1,y,count+1)
        elif grid[y][x-1] == 2 and count == self.zero_count:
            self.path_count += 1
        
        if grid[y+1][x] == 0:
            self.find_path(grid,x,y+1,count+1)
        elif grid[y+1][x] == 2 and count == self.zero_count:
            self.path_count += 1
            
        if grid[y-1][x] == 0:
            self.find_path(grid,x,y-1,count+1)
        elif grid[y-1][x] == 2 and count == self.zero_count:
            self.path_count += 1
            
        grid[y][x] = 0
            
        return
        
    
    def uniquePathsIII(self, grid) :
        
        self.path_count = 0
        
        self.max_x = len(grid[0])
        self.max_y = len(grid)
        
        for i in range(self.max_y):
            grid[i].insert(0,-1)
            grid[i].append(-1)
        
        bound = [-1 for n in range(self.max_x + 2)]
        grid.insert(0,bound)
        grid.append(bound)
        
        self.max_x += 2
        self.max_y += 2
        
        s_x, s_y, self.zero_count = self.get_info(grid)
        
        self.find_path(grid, s_x, s_y, 0)
        return self.path_count
        
a = Solution()
a.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]])
a.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]])
a.uniquePathsIII([[0,1],[2,0]])




```




## 999. template (easy medium hard)

評價及簡介

---

題目：

```

something

```

---

解答：
```python=

def template:

```