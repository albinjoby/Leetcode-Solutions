class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = bin(start)[2:]
        goal = bin(goal)[2:]
        count = 0

        if len(start) < len(goal):
            while len(start) < len(goal):
                start = '0' + start
        if len(start) > len(goal):
            while len(start) > len(goal):
                goal = '0' + goal
        
        for i in range(len(start)):
            if start[i] != goal[i]:
                count += 1

        return count