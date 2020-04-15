class Solution:
    def findMaxLength(self, nums):
        
        prefix_sum = {}
        prefix_sum[0] = -1
        diff = 0
        ans = 0
        
        for i in range(len(nums)):
            if(nums[i]==0):
                diff-=1
            else:
                diff+=1
            
            if diff in prefix_sum:
                ans = max(i - prefix_sum[diff],ans)
            else:
                prefix_sum[diff] = i
            
        return ans
    
a = Solution()

print (a.findMaxLength([0,1]))
print (a.findMaxLength([0,1,0]))
print (a.findMaxLength([]))
print (a.findMaxLength([0,0,0,0]))
print (a.findMaxLength([0,1,1,1,1,0,0]))