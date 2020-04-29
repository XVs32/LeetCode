class Solution:
    
    def countElements(self, arr):
        
        prev_num = None
        ans_counter = 0
        same_num_counter = 1
        
        for number in sorted(arr):
            
            if prev_num == number:
                same_num_counter += 1
                continue
                
            if prev_num == number - 1:
                ans_counter += same_num_counter
                
            prev_num = number
            same_num_counter = 1

        return ans_counter
        
a = Solution()

print (a.countElements([1,2,3]))
print (a.countElements([1,1,3,3,5,5,7,7]))
print (a.countElements([1,3,2,3,5,0]))
print (a.countElements([1,1,2,2]))
print (a.countElements([2,9,0,7,6,2,7,7,0]))


