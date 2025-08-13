class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        arr = ["(",")"]
        res = []
        def backtrack(path,open,close):
            if len(path) > n*2 or open > n or close > n:
                return
            if len(path) == n*2 and open == close == n:
                res.append("".join(path))
                return 
            for c in arr:
                if c == "(":
                    open += 1
                else:
                    close += 1
                path.append(c)
                if open >= close:
                    backtrack(path,open,close)
                if c == "(":
                    open -= 1
                else:
                    close -= 1
                path.pop()
            
        backtrack([],0,0)        
        return res
    