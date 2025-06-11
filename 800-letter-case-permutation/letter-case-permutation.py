class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        res = set()
        s = list(s)
        def backtrack(i):
            if i >= n:
                return 

            s[i] = s[i].upper()
            res.add(''.join(s))
            backtrack(i+1)
            s[i] = s[i].lower()
            res.add(''.join(s))
            backtrack(i+1)
            
        backtrack(0)
        return list(res)