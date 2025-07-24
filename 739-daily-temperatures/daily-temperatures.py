class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        i = 0
        for idx,temp in enumerate(temperatures):
            stack.append([temp,idx])
            while len(stack) > 1 and stack[-2][0] < stack[-1][0]:
                target = stack[-2][1]
                diff = stack[-1][1] - target
                stack[-2] = stack[-1]
                stack.pop()
                res[target] = diff
        return res