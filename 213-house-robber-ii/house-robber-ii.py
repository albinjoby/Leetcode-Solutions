class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[-1]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        def check(arr):
            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0],arr[1])
            for i in range(2,len(arr)):
                dp[i] = max(dp[i-1],arr[i]+dp[i-2])

            return dp[-1]
        
        return max(check(nums[:-1]),check(nums[1:]))
