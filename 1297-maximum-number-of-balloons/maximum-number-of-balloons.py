class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic = {}
        for letter in text:
            if letter in dic:
                dic[letter] += 1
            else:
                dic[letter] = 1

        count = 0
        while True:
            for letter in "balloon":
                if letter in dic and dic[letter] > 0:
                    dic[letter] -= 1
                else:
                    return count
            count += 1


        