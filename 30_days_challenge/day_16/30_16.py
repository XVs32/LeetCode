class Solution:
    
    
    def checkValidString(self, s):
        
        left = 0
        right = 0
        uni = 0
        
        for i in s:
            if i == "(":
                left += 1
            elif i == ")":
                right += 1
                if left + uni < right:
                    return False
            else:
                uni += 1
        
        if abs(left - right) > uni:
            return False
        
        
        left = 0
        right = 0
        uni = 0
        
        
        
        for i in reversed(s):
            if i == "(":
                left += 1
                if right + uni < left:
                    return False
            elif i == ")":
                right += 1
            else:
                uni += 1
        
        if abs(left - right) > uni:
            return False
        
        return True
    
a = Solution()

print (a.checkValidString("()"))
print (a.checkValidString("(*)"))
print (a.checkValidString("(*))"))
print (a.checkValidString(")("))
print (a.checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*"))
