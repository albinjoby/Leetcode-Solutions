class Solution:
    def countBits(self, n: int) -> List[int]:
        offset = 1
        dp = [0] * (n+1)
        for i in range(1,len(dp)):
            if offset * 2 == i:
                offset *= 2
            dp[i] = dp[i-offset] + 1

        return dp