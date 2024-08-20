class Solution(object):
    def sequentialDigits(self, low, high):
        vals = range(1,10)
        lst = []
        for i in range(len(vals)):
            for j in range(i+1,len(vals)+1):
                val = int(''.join(map(str, vals[i:j])))
                if low <= val <= high:
                    lst.append(val)
            
        lst.sort()
        return lst
                
                