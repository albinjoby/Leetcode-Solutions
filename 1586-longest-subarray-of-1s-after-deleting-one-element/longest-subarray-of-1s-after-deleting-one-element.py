class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res, count, zeros, l = 0, 0, 0, 0

        for r in range(len(nums)):
            zeros += 1 if nums[r] == 0 else 0
            while zeros > 1:
                zeros -= 1 if nums[l] == 0 else 0
                l += 1
            res = max(res,r-l)

        return res