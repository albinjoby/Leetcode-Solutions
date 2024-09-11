class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        ans = start ^ goal
        while ans:
            ans = ans & (ans-1)
            count += 1

        return count