class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) % 2 == 0 and len(nums2) % 2 == 0:
            return 0 
        
        res = 0
        if len(nums2) % 2 == 1:
            for num in nums1:
                res ^= num
            
        if len(nums1) % 2 == 1:
            for num in nums2:
                res ^= num

        return res