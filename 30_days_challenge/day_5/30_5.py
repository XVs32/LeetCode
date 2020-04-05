class Solution:
    def maxProfit(self, prices):
        
        profit = 0
        lo = 0x7fffffff
        length = len(prices)
        
        i = 0
        while i < length:
            
            while i < length and lo > prices[i]:
                lo = prices[i]
                i += 1
                
            if i == length:
                break
                
            hi = prices[i]
            i += 1
            
            while i < length and hi < prices[i]:
                hi = prices[i]
                i += 1
                
            profit += hi - lo
            lo = 0x7fffffff
            
        if profit < 0:
            profit = 0
        
        return profit
        
a = Solution()
print (a.maxProfit([7,1,5,3,6,4]))
print (a.maxProfit([1,2,3,4,5]))
print (a.maxProfit([7,6,4,3,1]))

