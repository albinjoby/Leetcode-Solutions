class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True

        for i in range(len(goal)):
            check = s[i:] + s[:i]
            if check == goal:
                return True

        return False