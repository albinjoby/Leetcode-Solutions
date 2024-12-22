class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        res = set()
        i = 0

        while True:
            val_x = x**i
            if val_x > bound:
                break

            j = 0
            while True:
                val_y = y**j
                if val_x + val_y > bound:
                    break

                res.add(val_x + val_y)

                if y == 1:
                    break
                j += 1

            if x == 1:
                break
            i += 1

        return list(res)