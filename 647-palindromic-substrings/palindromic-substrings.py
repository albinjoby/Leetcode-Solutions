class Solution:
    def countSubstrings(self, s: str) -> int:
        # seen = set()
        count = 0
        for i in range(len(s)):
            # Finding palindromes of odd length
            l,r = i,i
            while l > -1 and r < len(s) and s[l] == s[r]:
                # seen.add((l,r))
                count += 1
                l -= 1
                r += 1
            # Finding palindromes of even length
            l,r = i,i+1
            while l > -1 and r < len(s) and s[l] == s[r]:
                # seen.add((l,r))
                count += 1
                l -= 1
                r += 1
        # print(seen)
        # return len(seen)
        return count