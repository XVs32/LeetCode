class Solution:
    def stringShift(self, s, shift):
        
        count = 0
        
        for op in shift:
            
            if op[0] == 0:
                count += op[1]
            else:
                count -= op[1]
            
        count %= len(s)
        
        s = s[count:] + s[:count]
        
        return s