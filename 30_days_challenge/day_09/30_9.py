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

