class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        res = set()
        res.add(s)
        s = list(s)
        def backtrack(i):
            if i >= n:
                return 

            if s[i].isalpha():
                s[i] = s[i].upper()
                res.add(''.join(s))
                backtrack(i+1)
                s[i] = s[i].lower()
                res.add(''.join(s))
                backtrack(i+1)
            else:
                backtrack(i+1)
            
        backtrack(0)
        return list(res)