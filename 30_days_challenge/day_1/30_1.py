class Solution:

    def singleNumber(self, nums):
        
        table = {}
        
        for i in range(len(nums)):
            
            if not table.__contains__(nums[i]):
                table[nums[i]] = 1;
            else:
                table.pop(nums[i])
    
        return list(table)[0]
    
        
        
a = Solution()
print("%s" % a.singleNumber([2,2,1]))
print("%s" % a.singleNumber([4,1,2,1,2]))
print("%s" % a.singleNumber([4,1,2,1,2]))

