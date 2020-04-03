class Solution:
    def maxSubArray(self, nums):
        sums_previous = 0
        sums_now = 0
        max_sum = nums[0] 

        for i in range(len(nums)):
            sums_now = sums_previous + nums[i] 
            
            if max_sum < sums_now:
                max_sum = sums_now
            
            if sums_now < 0 :
                sums_now = 0
                
            sums_previous = sums_now
        return max_sum
        
        
a = Solution()
print (a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print (a.maxSubArray([1,2,3,4,5,6,7,8,9,10]))
print (a.maxSubArray([-1,-2,-3,-4,-5,-6]))
print (a.maxSubArray([-2,1]))
print (a.maxSubArray([-2,-1]))