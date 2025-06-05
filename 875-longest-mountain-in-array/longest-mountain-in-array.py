class Solution:
    def longestMountain(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        res = 0
        l, r = 0, 1
        n = len(nums)
        
        while r < len(nums):
            uphill, downhill = False, False
            
            #check for uphill
            if nums[r-1] < nums[r]:
                uphill = True
                # find the peak of hill
                while r+1 < n and nums[r] < nums[r+1]:
                    r += 1
                
            # find for downhill
            if uphill and r+1 < n and nums[r] > nums[r+1]:
                downhill = True
                # find bottom fo hill
                while r+1 < n and  nums[r] > nums[r+1]:
                    r += 1
                
            # check lenght of mountain if there was uphill and downhill
            if uphill and downhill:
                res = max(res, r-l+1)
                l = r
                r += 1
            else:
                if uphill:
                    l += 1
                    r = l
                else:
                    l = r
                    r += 1

        return res
                    