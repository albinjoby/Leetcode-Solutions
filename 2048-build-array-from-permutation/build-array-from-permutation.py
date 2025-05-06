class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        for i in range(n):
            if 0 <= i < n:
                res[i]  = nums[nums[i]]

        return res