class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        
        cache = {
            0: nums[0],
            1: max(nums[0],nums[1])
        }

        def check(i):
            if i in cache:
                return cache[i]
            cache[i] = max(nums[i] + check(i-2) , check(i-1))
            return cache[i]

        return check(n-1)