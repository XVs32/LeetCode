class Solution:
    def productExceptSelf(self, nums):
        
        length = len(nums)
        
        prefix_pro = [1] * (length + 1)
        suffix_pro = [1] * (length + 1)
        
        for i in range(length):
            prefix_pro[i + 1] = nums[i] * prefix_pro[i]
            suffix_pro[i + 1] = nums[length - 1 - i] * suffix_pro[i]
        
        for i in range(length):
            nums[i] = prefix_pro[i] * suffix_pro[length - i - 1]
            
        return nums
    
a = Solution()

print (a.productExceptSelf([1,2,3,4]))
