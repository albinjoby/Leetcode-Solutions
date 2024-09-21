class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        def check(num):
            for i in range(0,10):
                val = num*10+i
                if val <= n:
                    res.append(val)
                    check(val)
                else:
                    return

        for num in range(1,n+1):
            if num <= n and num not in res:
                res.append(num)
                check(num)

        return res
