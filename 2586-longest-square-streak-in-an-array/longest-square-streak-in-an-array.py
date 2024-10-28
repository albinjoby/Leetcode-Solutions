class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        seen = set(nums)

        longes_streak = 1
        for num in nums:
            streak = 1
            while num * num in seen:
                streak += 1
                num = num * num
            longes_streak = max(longes_streak, streak)  

        return -1 if longes_streak == 1 else longes_streak