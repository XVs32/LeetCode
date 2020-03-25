class Solution:
    def summaryRanges(self, nums) :
        if not nums:
            return nums
        ans = []
        count = 1
        start = nums[0]
        end = nums[0]
        for i in range(1,len(nums)):
            
            if end == nums[i] - 1:
                count += 1
                end = nums[i]
            else:
                if count == 1:
                    ans.append(str(start))
                else:
                    ans.append(str(start) + "->" + str(end))
                    
                count = 1
                start = nums[i]
                end = nums[i]
        
        if count == 1:
            ans.append(str(start))
        else:
            ans.append(str(start) + "->" + str(end))
        
        return ans
        
a = Solution()
print (a.summaryRanges([0,1,2,4,5,7]))
print (a.summaryRanges([0,2,3,4,6,8,9]))
print (a.summaryRanges([]))
        