class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        prefix_sum = {}
        prefix_sum[50000] = [-1,-1]
        ones = 0
        zeros = 0
        length = len(nums)
        i = 0
        while i < length:
            
            ones += nums[i] & 1
            zeros += ~nums[i] & 1
            
            diff = ones - zeros + 50000
            
            if not prefix_sum.__contains__(diff):
                prefix_sum[diff] = [i,i]
            else:
                prefix_sum[diff][0] = min(prefix_sum[diff][0],i)
                prefix_sum[diff][1] = max(prefix_sum[diff][1],i)
            
            
            i += 1
        
        ans = 0
        for perfix in prefix_sum.values():
            ans = max(perfix[1] - perfix[0],ans)
            
        return ans
    
a = Solution()

print (a.findMaxLength([0,1]))
print (a.findMaxLength([0,1,0]))
print (a.findMaxLength([]))
print (a.findMaxLength([0,0,0,0]))
print (a.findMaxLength([0,1,1,1,1,0,0]))