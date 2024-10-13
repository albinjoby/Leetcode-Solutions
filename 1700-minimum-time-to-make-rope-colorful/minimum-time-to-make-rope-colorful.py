from typing import List

class Solution:
    def minCost(self, colors: str, time: List[int]) -> int:
        stack = []
        res = 0

        for i, color in enumerate(colors):
            if stack and stack[-1][0] == color:  # Check the last color in the stack
                # If consecutive same-colored balloons, add the smaller cost
                if stack[-1][1] < time[i]:
                    res += stack[-1][1]
                    stack.pop()
                    stack.append((color, time[i]))  # Push the current balloon with its cost
                else:
                    res += time[i]
            else:
                stack.append((color, time[i]))  # Push the color and cost to the stack

        return res