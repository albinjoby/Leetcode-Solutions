class Solution:
    def rob(self, nums: List[int]) -> int:
        def check(arr):
            if len(arr) == 0:
                return 0
            if len(arr) == 1:
                return arr[-1]
            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0],arr[1])
            for i in range(2,len(arr)):
                dp[i] = max(dp[i-1],arr[i]+dp[i-2])

            return dp[-1]
        
        return max(check(nums[:-1]),check(nums[1:])) if len(nums) > 2 else max(nums)
