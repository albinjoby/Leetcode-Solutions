class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res, count = 0, 0
        for n in nums:
            if n-1 not in nums:
                l = 0
                while n+l in nums:
                    l += 1
                res = max(res,l)

        return res