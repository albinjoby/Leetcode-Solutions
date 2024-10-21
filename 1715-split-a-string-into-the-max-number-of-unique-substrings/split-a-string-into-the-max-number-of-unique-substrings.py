class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        used = set()

        def dfs(i):
            if i == len(s):
                return 0

            res = 0
            for j in range(i,len(s)):
                substr = s[i:j+1]
                if substr in used:
                    continue
                used.add(substr)
                res = max(res,1+dfs(j+1))
                used.remove(substr)
            return res

        return dfs(0)