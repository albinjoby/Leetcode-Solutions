class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # if lenght of the num2 is even then we dont need to use nums1
        # if there are even no of numbers then they can be ignored
        if len(nums1) % 2 == 0 and len(nums2) % 2 == 0:
            return 0 

        counter = Counter(nums2)

        temp = 0
        for num in nums2:
            if counter[num] % 2 == 1:
                temp ^= num

        if len(nums2) % 2 == 0:
            return temp

        counter = Counter(nums1) 
        res = 0 
        for num in nums1:
            if counter[num] % 2 == 1:
                res ^= (num ^ temp)

        return res