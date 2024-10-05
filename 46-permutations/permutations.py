class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, arr = [],[]

        def backtrack():
            if len(arr) == n:
                res.append(arr[:])
                return

            for x in nums:
                if x not in arr:
                    arr.append(x)
                    backtrack()
                    arr.pop()


        backtrack()

        return res