class Solution:
    def majorityElement(self, nums):
		
        if not nums:
            return []
        
        ans = []
        max_num = max(nums)
        min_num = min(nums)
        pass_bound = len(nums)/3
        if max_num - min_num < 50000:
            map_count=[0]*(max_num - min_num + 1)
            for i in range(len(nums)):
                map_count[nums[i]- min_num] += 1
            for i in range(max_num - min_num + 1):
                if map_count[i] > pass_bound:
                    ans.append(i + min_num)		
            return ans
        else:
            hash_count = {}
            for i in range(len(nums)):
                if not hash_count.__contains__(nums[i]):
                    hash_count[nums[i]] = 1;
                else:
                    hash_count[nums[i]] += 1
            for i, j in hash_count.items():
                if j > pass_bound:
                    ans.append(i)
            return ans
    
a = Solution()
print (a.majorityElement([3,2,3]))
print (a.majorityElement([1,1,1,3,3,2,2,2]))
print (a.majorityElement([]))
print (a.majorityElement([0,-1,2,-1]))
