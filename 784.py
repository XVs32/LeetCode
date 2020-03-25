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