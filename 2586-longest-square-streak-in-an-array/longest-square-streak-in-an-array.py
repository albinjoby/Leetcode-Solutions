class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        seen = set(nums)
        longest_streak = 0
        for num in seen:
            streak = 1
            while num * num in seen:
                num = num * num
                streak += 1
            longest_streak = max(longest_streak, streak)
        
        return -1 if longest_streak == 1 else longest_streak