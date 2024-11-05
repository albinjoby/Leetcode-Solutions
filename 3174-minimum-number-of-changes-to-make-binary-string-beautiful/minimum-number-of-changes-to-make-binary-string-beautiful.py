class Solution:
    def minChanges(self, s: str) -> int:
        # count = 0
        # for i in range(0,len(s),2):
        #     if s[i] != s[i+1]:
        #         count += 1
        
        # return count

        return sum([s[i]!=s[i+1] for i in range(0,len(s),2)])