class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        max_arr = [0] * len(nums)
        i = len(nums)-1
        prev = 0
        for n in reversed(nums):
            max_arr[i] = max(n,prev)
            prev = max_arr[i]
            i -= 1

        res = 0
        l = 0
        for r in range(len(nums)):
            while nums[l] > max_arr[r]:
                l += 1
            res = max(res, r-l)

        return res