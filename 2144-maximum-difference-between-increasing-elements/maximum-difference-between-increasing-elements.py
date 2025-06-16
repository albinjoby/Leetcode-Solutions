class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = -1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if 0 <= i < j < len(nums) and nums[i] < nums[j]:
                    res = max(res, nums[j] - nums[i])

        return res