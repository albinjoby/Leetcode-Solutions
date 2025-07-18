class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        seen = set()
        def backtrack(path,total):
            if total == target:
                val = tuple(sorted(path[:]))
                if val not in seen:
                    res.append(path[:])
                    seen.add(val)
            if total > target:
                return
            for num in nums:
                path.append(num)
                backtrack(path,total+num)
                path.pop()

        backtrack([],0)
        return res