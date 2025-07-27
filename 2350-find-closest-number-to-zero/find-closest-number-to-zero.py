class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = nums[0]
        current_min = float('inf')
        for num in nums:
            if abs(0 - num) < current_min:
                current_min = abs(0 - num)
                res = num
            
        if res < 0 and -res in nums:
            return -res
        return res