class Solution:
    def moveZeroes(self, nums):
        
        fast_id = 0
        slow_id = 0
        length = len(nums)
        
        while slow_id + fast_id < length:
            
            if nums[slow_id + fast_id] == 0:
                fast_id += 1
                continue
                
            nums[slow_id] = nums[slow_id + fast_id]
            slow_id += 1
            
        while slow_id < length:
            nums[slow_id] = 0
            slow_id += 1
        
        return nums
        
a = Solution()
print (a.moveZeroes([0,1,0,3,12]))
print (a.moveZeroes([0,0,1]))
print (a.moveZeroes([0,1,0]))
print (a.moveZeroes([1,0,0]))
print (a.moveZeroes([-2,-1]))