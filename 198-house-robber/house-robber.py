class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def check(arr):
            if not arr:
                return 0
            
            if len(arr) == 1:
                return arr[0]

            input = tuple(arr)
            if input in cache:
                return cache[input]

            cache[input] = max(arr[0] + check(arr[2:]), check(arr[1:]))
            return cache[input]

        return check(nums)