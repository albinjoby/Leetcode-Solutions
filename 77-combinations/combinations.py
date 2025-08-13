class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(idx,path):
            if len(path) == k:
                res.append(path[:])
                return
            for num in range(idx,n+1):
                path.append(num)
                backtrack(num+1,path[:])
                path.pop()
        
        backtrack(1,[])
        return res
