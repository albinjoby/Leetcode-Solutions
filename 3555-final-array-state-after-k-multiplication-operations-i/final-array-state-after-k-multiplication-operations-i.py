class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        for _ in range(k):
            idx = nums.index(min(nums))
            nums[idx] = nums[idx] * multiplier
        return nums