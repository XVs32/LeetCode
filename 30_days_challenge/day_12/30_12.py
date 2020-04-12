from heapq import *

class Solution:
    def lastStoneWeight(self, stones):
        i = len(stones)
        
        j=0
        while j < i:
            stones[j] *= -1
            j+=1
            
        heapify(stones)

        while i > 1:
            a = heappop(stones)
            b = heappop(stones)
            
            if a != b:
                heappush(stones, a-b)
                i -= 1
            else:
                i -= 2
        
        if i == 0:
            return 0
        else:
            return -heappop(stones)

a = Solution()

print (a.lastStoneWeight([2,7,4,1,8,1]))