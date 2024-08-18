class Solution(object):
    def nthUglyNumber(self, n):
        lst = [1]
        i2, i3, i5 = 0, 0, 0
        for _ in range(1,n):
            next_val = min(lst[i2]*2,
                            lst[i3]*3,
                            lst[i5]*5)
            lst.append(next_val)
            if next_val == lst[i2]*2:
                i2 += 1
            if next_val == lst[i3]*3:
                i3 +=1
            if next_val == lst[i5]*5:
                i5 +=1

        return lst[n-1]