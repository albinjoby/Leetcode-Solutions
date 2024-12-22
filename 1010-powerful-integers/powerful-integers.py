class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        valsx, valsy = set(), set()
        k = 0
        while k < bound:
            val = x**k
            if val < bound:
                valsx.add(val)
            else:
                break
            k += 1

        k = 0
        while k < bound:
            val = y ** k
            if val < bound:
                valsy.add(val)
            else:
                break
            k += 1

        valsx = list(valsx)
        valsy = list(valsy)

        res = set()

        for i in range(len(valsx)):
            for j in range(len(valsy)):
                val = valsx[i] + valsy[j]
                if val <= bound:
                    res.add(val)
            
        res = list(res)
        return res