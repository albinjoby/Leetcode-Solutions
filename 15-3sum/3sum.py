class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        seen = set()
        for i in range(len(nums)):
            num1 = nums[i]
            j, k = i+1,len(nums)-1
            while j < k:
                num2, num3 = nums[j], nums[k]
                total = num1 + num2 + num3
                if total == 0:
                    seen.add(tuple([num1,num2,num3]))
                    k -= 1
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    j += 1
                
        return [list(val) for val in seen]


