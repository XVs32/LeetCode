# day_9: Backspace String Compare

###### tags: `online_judge`, `python3`

給定兩個只包含字母和```#```的字串，其中```#```代表 backspace，問兩個字串在處理完 backspace 後一否一致。

從字串末尾開始掃描，即可把 backspace 轉化為 delete，這時候就變成遇到```#```就無視下一個字元了。
然而```#```可能會連續出現，所以需要記錄```#```連續出現多少次，然後無視同樣多個字元。

---

## 題目

```
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

Note:

    1 <= S.length <= 200
    1 <= T.length <= 200
    S and T only contain lowercase letters and '#' characters.

Follow up:

    Can you solve it in O(N) time and O(1) space?
```

---

## 解答

```python=
class Solution:
    def backspaceCompare(self, S, T):
        
        S += "a"
        T += "a"
        
        i = len(S) -1
        j = len(T) -1
        
        while i > -1 and j > -1:
                
            if S[i] != T[j]:
                return False
                
            S_backspace = 1
            while S_backspace > 0 and i > -1:
                i -= 1
                S_backspace -= 1
                if S[i] == "#":
                    S_backspace += 2
                
            T_backspace = 1
            while T_backspace > 0 and j > -1:
                j -= 1
                T_backspace -= 1
                if T[j] == "#":
                    T_backspace += 2
        
        while i > -1 and S[i] == "#":
            S_backspace = 1
            while S_backspace > 0 and i > -1:
                i -= 1
                S_backspace -= 1
                if S[i] == "#":
                    S_backspace += 2

        while j > -1 and T[j] == "#":
            T_backspace = 1
            while T_backspace > 0 and j > -1:
                j -= 1
                T_backspace -= 1
                if T[j] == "#":
                    T_backspace += 2
                
        """print(S[i])
        print(T[j])"""
        
        if i < 0 and j < 0:
            return True
        else: 
            return False
        
a = Solution()

print (a.backspaceCompare("ab#c","ad#c"))
print (a.backspaceCompare("ab##","c#d#"))
print (a.backspaceCompare("a##c","#a#c"))
print (a.backspaceCompare("a#c","b"))
print (a.backspaceCompare("bxj##tw","bxo#j##tw"))
```

---
### 成績

![](https://i.imgur.com/OI4OumT.png)



---