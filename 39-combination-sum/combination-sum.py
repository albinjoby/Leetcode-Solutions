class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        arr = []

        def backtrack(path,total):
            if total > target:
                return
            if total == target:
                arr.append(path[:])
            for num in candidates:
                path.append(num)
                backtrack(path, total+num)
                path.pop()

        backtrack([],0)
        seen = set()
        res = []
        for item in arr:
            val = tuple(sorted(item))
            if val not in seen:
                res.append(item)
                seen.add(val)
        
        return res