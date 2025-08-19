class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        res = 0
        for num in nums:
            if num == 0:
                count +=1
            else:
                res += (count*(count+1))//2 if count > 0 else 0
                count = 0
        res += (count*(count+1))//2 if count > 0 else 0
        return res
