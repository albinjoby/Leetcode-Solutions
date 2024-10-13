from typing import List

class Solution:
    def minCost(self, colors: str, time: List[int]) -> int:
        res = 0  # Initialize result for total removal cost

        for i in range(1, len(colors)):  # Start from 1 to compare with previous balloon
            if colors[i] == colors[i - 1]:  # If the current balloon is the same color as the previous
                res += min(time[i], time[i - 1])  # Add the smaller cost to the result
                time[i] = max(time[i], time[i - 1])  # Keep the larger time for future comparison

        return res
        