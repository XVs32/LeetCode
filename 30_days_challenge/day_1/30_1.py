class Solution:

    def singleNumber(self, nums):
        
        ans = 0
        for i in nums:
            ans = ans ^ i
        return ans
        
        
a = Solution()
print("%s" % a.singleNumber([2,2,1]))
print("%s" % a.singleNumber([4,1,2,1,2]))
print("%s" % a.singleNumber([-1]))

