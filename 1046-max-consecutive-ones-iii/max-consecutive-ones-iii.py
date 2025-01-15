class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_window_len = 0
        zeros = 0
        l,r = 0,0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1
            
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            max_window_len = max(max_window_len, r-l+1)
        
        return max_window_len
