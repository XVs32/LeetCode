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


