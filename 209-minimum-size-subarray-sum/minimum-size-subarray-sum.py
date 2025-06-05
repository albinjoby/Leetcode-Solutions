class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        length = float('inf')
        total = 0
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                length = min(length, r-l+1)
                total -= nums[l]
                l += 1

        return 0 if length == float('inf') else length