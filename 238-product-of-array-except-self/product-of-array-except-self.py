class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # val = 1
        # prefix = []
        # for num in nums:
        #     val *= num
        #     prefix.append(val)
        # print(prefix)
        # val = 1
        # postfix = [1] * len(nums)
        # for i in range(len(nums)-1,-1,-1):
        #     val *= nums[i]
        #     postfix[i] = val
        # print(postfix)
        # res = [1]*len(nums)
        # for i in range(len(nums)):
        #     if -1 < i-1 and i+1 < len(nums):
        #         res[i] = prefix[i-1] * postfix[i+1]
        #     elif -1 < i-1:
        #         res[i] = prefix[i-1]
        #     else:
        #         res[i] = postfix[i+1]
        # return res

        res = []
        val = 1
        for num in nums:
            res.append(val)
            val = val*num
        print(res)
        val = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= val
            val = val*nums[i]
        print(res)
        return res
