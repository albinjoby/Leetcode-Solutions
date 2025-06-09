class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(n+1):
            count = 0
            while num:
                count += num % 2
                num //= 2
            res.append(count)

        return res