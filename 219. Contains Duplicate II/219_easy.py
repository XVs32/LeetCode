class Solution:
    def containsNearbyDuplicate(self, nums, k):
        
        table = {}
        
        for i in range(len(nums)):
            
            if not table.__contains__(nums[i]):
                table[nums[i]] = i;
            elif i - table[nums[i]] <= k:
                return True
            else :
                table[nums[i]] = i;

        return False
	
a = Solution()
print (a.containsNearbyDuplicate([1,2,3,1],3))
print (a.containsNearbyDuplicate([1,0,1,1],1))
print (a.containsNearbyDuplicate([1,2,3,1,2,3],2))
print (a.containsNearbyDuplicate([1,2,3],0))