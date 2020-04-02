class Solution:
    def isHappy(self,n):
        ans = 0
        record = {}
        while True:
            if not record.__contains__(n):
                record[n] = True
                while n != 0:
                    ans += (n % 10) * (n % 10)
                    n = (int)(n / 10)
                n = ans
                ans = 0
            else:
                if n == 1:
                    return True
                else:
                    return False

a = Solution()
print (a.isHappy(19))
print (a.isHappy(1))
print (a.isHappy(0))
