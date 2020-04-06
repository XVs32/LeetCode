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


