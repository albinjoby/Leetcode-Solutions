class Solution:
    def getLucky(self, s: str, k: int) -> int:#a = 97
        res = []
        for letter in s:
            val = ord(letter) - 96
            res.append(str(val))

        res = "".join(res)

        for _ in range(k):
            val = 0
            for num in res:
                val += int(num)
            res = str(val)
            print(res)

        return int(res)


        