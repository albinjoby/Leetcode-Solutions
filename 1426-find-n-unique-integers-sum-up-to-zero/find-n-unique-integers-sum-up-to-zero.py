class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        if n % 2 != 0:
            res.append(0)
        for i in range(1,n):
            if len(res) == n:
                break
            res.append(i)
            res.append(-i)

        return res