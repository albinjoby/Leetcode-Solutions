class Solution(object):
    def findClosestNumber(self, nums):
        res = float('inf')
        for num in nums:
            if abs(num) < abs(res):
                res = num
            elif abs(num) == abs(res):
                res = max(res,num)
                
        return res