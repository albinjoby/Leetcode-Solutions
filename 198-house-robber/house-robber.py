class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def check(arr):
            if not arr:
                return 0
            if len(arr) == 1:
                return arr[0]
            inputs = tuple(arr)
            if inputs in memo:
                return memo[inputs]
            memo[inputs] = max(arr[0] + check(arr[2:]), check(arr[1:]) )
            return memo[inputs]

        return check(nums)
