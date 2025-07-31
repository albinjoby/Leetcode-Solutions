class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0] * len(height)
        for i in range(1,len(height)):
            max_left[i] = max(max_left[i-1],height[i-1])
        print(max_left)
        max_right = [0] * len(height)
        for i in range(len(height)-2,-1,-1):
            max_right[i] = max(max_right[i+1],height[i+1])
        print(max_right)
        res = [0]*len(height)
        for i in range(len(height)):
            res[i] = min(max_right[i],max_left[i]) - height[i]
        print(res)
        return sum([num for num in res if num > 0])













        # res = 0
        # for i in range(1,len(height)-1):
        #     if height[i-1] > height[i]:
        #         diff = height[i-1] - height[i]
        #         target = height[i-1]
        #         while diff:
        #             # print(target)
        #             # print("water fillabel at index ",i)
        #             l = i-1
        #             r = i+1
        #             while l < r and r < len(height) and height[r] < target:
        #                 r += 1
        #             if r != len(height):
        #                 res += r-l-1
        #             # print(l,r,"value =",r-l-1)
        #             target -= 1
        #             diff -= 1
                
        # return res

