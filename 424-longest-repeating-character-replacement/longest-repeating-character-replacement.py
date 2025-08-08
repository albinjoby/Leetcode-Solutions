class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        arr = [0] * 26
        for r in range(len(s)):
            arr[ord(s[r]) - ord('A')] += 1
            while (r-l+1) - max(arr) > k:
                arr[ord(s[l]) - ord('A')] -= 1
                l += 1
            res = max(res, r-l+1)

        return res