class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        n = len(nums)-1

        memo = {0:nums[0],
                1:max(nums[0],nums[1]),
        }
        
        def dp(n):
            if n in memo:
                return memo[n]
            memo[n] = max(nums[n] + dp(n-2), dp(n-1))
            return memo[n]

        return dp(n)

        