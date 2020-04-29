# day_6: Group Anagrams

###### tags: `online_judge`, `python3`

給定一組字串，把具有相同字元（不限順序）的字串分在同一組，並輸出各組字串。

例如 ```eat``` 和 ```tea``` 在同一組。
而 ```eat``` 和 ```eaf``` 則不在同一組。

這題有兩種解法，分別是陣列或排序。

陣列解法是為每個字串建立長度為 26 的 int 陣列。統計其中各個字母的出現次數，並和其他字串的統計比對。例如有字串```aacd```，則其統計陣列為```[2,0,1,1,0,0,...,0]```。
為求加速可以建立 hash table，以字串 ASCII sum 作為 key。免去每次和其餘所有字串統計陣列比對。
但考慮極端情況，若所有字串的 ASCII sum 都重複，而且所有字串都不同組，那麼比對次數將會是 O(N^2)。

排序解法為每個字串先進行排序，並以排序後的字串為 key 建立 hash table。
因為如果兩個字串同有相同的字元，那麼兩個字串排序後必定相同。
例：```eat``` 和 ```tea``` 在排序後都是 ```aet```。



---

## 題目

```
Given an array of strings, group anagrams together.

Example 1:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```

---

## 解答

python array version:
```python=
class Solution:
    def groupAnagrams(self, strs):
        
        sum_map = {}
        str_map = []
        str_info_length = 0
        str_ans = []
        
        for string in strs:
            
            ascii_map = [0]*27
            length = len(string)
            i = 0
            while i < length:
                ascii_map[26] += (ord(string[i])-97)
                ascii_map[ord(string[i])-97] += 1
                i += 1
            
            if not sum_map.__contains__(ascii_map[26]):
                str_map.append(ascii_map)
                str_ans.append([string])
                sum_map[ascii_map[26]] = []
                sum_map[ascii_map[26]].append(str_info_length)
                str_info_length += 1
                
            else:
                flag = False
                for posible_case in sum_map[ascii_map[26]]:
                    
                    if str_map[posible_case] == ascii_map:
                        str_ans[posible_case].append(string)
                        flag = True
                        break
                if flag == False:
                    str_map.append(ascii_map)
                    str_ans.append([string])
                    
                    sum_map[ascii_map[26]].append(str_info_length)
                    str_info_length += 1

        return str_ans
        
a = Solution()

"""print (a.groupAnagrams(["eat", "eat", "ate"]))"""

"""print (a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))"""
print (a.groupAnagrams(["vow","pam","vic","bee","ken","jay","oft","sue","joy","yuk","sac","mac","inc","big","icy","bus","lob","flo","day","aol","eel","rex","jug","man","cod","mix","guy","ken"]))
```

python sorting version:
```python=
class Solution:
    
    def groupAnagrams(self, strs):
        
        sort_map = {}
        ans_length = 0
        ans = []
        
        for string in strs:
            
            sorted_string = ""
            sorted_string = sorted_string.join(sorted(string))
            
            if sorted_string not in sort_map:
                sort_map[sorted_string] = ans_length
                ans.append([string])
                ans_length += 1
                
            else:
                ans[sort_map[sorted_string]].append(string)
                
        return ans
        
a = Solution()

print (a.groupAnagrams(["eat", "eat", "ate"]))
print (a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print (a.groupAnagrams(["vow","pam","vic","bee","ken","jay","oft","sue","joy","yuk","sac","mac","inc","big","icy","bus","lob","flo","day","aol","eel","rex","jug","man","cod","mix","guy","ken"]))
```

---
### 成績
Array version:
![](https://i.imgur.com/dhFOF8k.png)
Sorting version:
![](https://i.imgur.com/XCfDDyc.png)



---