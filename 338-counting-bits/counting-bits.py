class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(0,n+1):
            res.append(bin(num).count("1"))

        return res