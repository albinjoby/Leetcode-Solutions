class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        heat_map = [0]*len(nums)
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                heat_map[i] = heat_map[i-1] + 1
        print(heat_map)
        for i in range(len(nums)-2,-1,-1):
            if nums[i] > nums[i+1]:
                heat_map[i] = heat_map[i] + heat_map[i+1]
        print(heat_map)
        max_val,max_idx = 0,0
        for i in range(len(heat_map)):
            if heat_map[i] > max_val:
                max_val = heat_map[i]
                max_idx = i            
        
        return max_idx