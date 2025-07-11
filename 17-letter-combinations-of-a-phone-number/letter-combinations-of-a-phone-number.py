class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        values = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        def backtrack(path,idx):
            if len(path) == len(digits):
                res.append("".join(path[:]))
            if idx > len(digits)-1:
                return
            for char in values[digits[idx]]:
                path.append(char)
                backtrack(path,idx+1)
                path.pop()

        backtrack([],0)
        return res
