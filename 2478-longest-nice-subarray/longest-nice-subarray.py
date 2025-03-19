class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = 0
        count = 0
        l = 0
        for r in range(len(nums)):
            while count & nums[r]:
                count ^= nums[l]
                l += 1
            count |= nums[r]
            res = max(res, r-l+1)
        return res