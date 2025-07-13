class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backtrack(path,total,idx):
            if len(path) == k and total == n:
                res.append(path[:])
                return
            if len(path) > k or total > n:
                return
            for i in range(idx,10):
                path.append(i)
                backtrack(path,total + i,i+1)
                path.pop()
            
        backtrack([],0,1)
        return res