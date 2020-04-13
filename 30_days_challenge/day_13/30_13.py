class Solution:
    def findMaxLength(self, nums):
        
        prefix_sum = []
        
        for num in nums:
            prefix_sum.append([~num & 1, num & 1])
            print ([~num & 1, num & 1])
        
    
a = Solution()

print (a.findMaxLength([0,1]))
print (a.findMaxLength([0,1,0]))