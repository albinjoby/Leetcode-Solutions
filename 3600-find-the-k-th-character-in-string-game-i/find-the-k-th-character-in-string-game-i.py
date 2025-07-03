class Solution:
    def kthCharacter(self, k: int) -> str:
        def helper(string):
            res = list(string)
            for s in string:
                res.append(chr(ord(s)+1) if ord(s) < 112 else "a")
            return ''.join(res)
        
        string = "a"
        while len(string) < k:
            string = helper(string)

        return string[k-1]