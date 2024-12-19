class Solution(object):
    def maxChunksToSorted(self, arr):
        res = 0
        for i in range(len(arr)):
            if sum(arr[:i]) == (i * (i-1))//2:
                res += 1
        
        return res