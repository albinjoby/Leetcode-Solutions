class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        length = max(len(bin(start)[2:]),len(bin(goal)[2:]))
        start = bin(start)[2:].zfill(length)
        goal =  bin(goal)[2:].zfill(length)
        count = 0
 
        for i in range(len(start)):
            if start[i] != goal[i]:
                count += 1

        return count