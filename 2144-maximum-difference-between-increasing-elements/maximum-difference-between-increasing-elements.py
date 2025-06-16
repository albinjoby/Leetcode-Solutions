class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_val = nums[0]
        res = -1
        for r in range(1,len(nums)):
            print(min_val,nums[r],res)
            res = max(res, nums[r] - min_val)
            if nums[r] < min_val:
                min_val = nums[r]

        return res if res > 0 else -1