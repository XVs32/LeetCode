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

