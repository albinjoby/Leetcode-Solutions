class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1

        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= goal:
                goal = i
            
        return goal == 0



        # memo = {}
        # def check(idx):
        #     if idx in memo:
        #         return memo[idx]
        #     if idx == len(nums)-1:
        #         return True
        #     if idx >= len(nums):
        #         return False
        #     options = nums[idx]
        #     for i in range(1,options+1):
        #         curr = idx + i
        #         res = check(curr)
        #         memo[curr] = res
        #         if res == True:
        #             return True
        #     return False
        
        # return check(0)