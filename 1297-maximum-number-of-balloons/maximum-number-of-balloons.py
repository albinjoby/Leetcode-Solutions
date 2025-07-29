class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        res = 0
        counter = Counter(text)
        while True:
            for l in "balloon":
                if l not in counter or counter[l] < 1:
                    return res
                counter[l] -= 1
            res += 1