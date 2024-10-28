class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:   
        if len(s) == 1:
            return 1  
        longest_streak = 0
        seen = set()
        for i in range(len(s)-1):
            seen.add(s[i])
            j = i+1
            while s[j] not in seen:
                seen.add(s[j])
                if j+1 >= len(s):
                    break
                else:
                    j+=1
            longest_streak = max(longest_streak,len(seen))
            seen = set()
        
        return longest_streak