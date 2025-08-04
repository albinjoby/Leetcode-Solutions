class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,r = 1,num
        while l<=r:
            m = (l+r)//2
            val = m * m
            if val == num:
                return True
            elif val < num:
                l = m+1
            else:
                r = m-1
        
        return False