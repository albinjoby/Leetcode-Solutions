class Solution:
    def kthCharacter(self, k: int) -> str:
        def helper(string):
            res = string
            for s in string:
                res += chr(ord(s)+1) if ord(s) < 112 else "a"
            return res
        
        string = "a"
        while len(string) < k:
            string = helper(string)

        return string[k-1]