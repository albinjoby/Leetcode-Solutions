class Solution:
    def canBeValid(self, s: str, lock: str) -> bool:
        locked = []
        unlocked = []

        for i in range(len(s)):
            if lock[i] == "0":
                unlocked.append(i)
            elif s[i] == "(":
                locked.append(i)
            else:
                if locked:
                    locked.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False

        while locked and unlocked and unlocked[-1] > locked[-1]:
            locked.pop()
            unlocked.pop()

        return len(locked)==0 and len(unlocked)%2==0