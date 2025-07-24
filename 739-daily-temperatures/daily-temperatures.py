class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        i = 0
        for idx,temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                res[stack[-1][1]] = idx - stack[-1][1]
                stack.pop()
            stack.append([temp,idx])
        return res