class Solution:
    
    count = 0
    length = 0
    flag = 1
    max_id = 0
    
    def recursive(self, s, i):
        
        tem = 1
        
        while i + tem < self.length:
            
            if s[i + tem] == "*" or s[i + tem] == "+":
                tem += 1
                continue
            
            if s[i + tem] == "(":
                s = self.recursive(s, i + tem)
                tem += 1
            else:
                s = s[0:i] + "+" + s[i+1:]
                s = s[0:i + tem] + "+" + s[i + tem +1:]
                self.flag = 1
                break
        return s
        
    
    def checkValidString(self, s):
        
        self.length = len(s)
        
        while(True):
            
            star = 0
            i = 0
            while i < self.length:
                if s[i] == "*":
                    star += 1
                elif s[i] == ")":
                    star -= 1
                    if star < 0:
                        return False
                elif s[i] != "+":
                    break
                i += 1
            
            if i == self.length or self.flag == 0:
                break
                
            self.flag = 0
            s = self.recursive(s,i)
            
            """print(s)"""
        
        
        i = 0
        star = 0
        while i < self.length and s[i] != "(":
            i += 1
        
        while i < self.length:
            if s[i] == "*":
                star += 1
            elif s[i] == "(":
                star = min(star - 1,-1)
            i += 1
        if star < 0:
            return False
        
        return True
    
a = Solution()

print (a.checkValidString(""))
print (a.checkValidString("()"))
print (a.checkValidString("(*)"))
print (a.checkValidString("(*))"))
print (a.checkValidString(")("))
print (a.checkValidString("(*()"))
print (a.checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*"))
