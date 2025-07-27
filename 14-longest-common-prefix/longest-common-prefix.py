class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = len(strs[0])
        for s in strs:
            length = min(length,len(s))

        res = []
        i = 0
        while i < length:
            l = strs[0][i]
            for s in strs:
                if s[i] != l:
                    return "".join(res)
            res.append(l)
            i += 1
        
        return "".join(res)
