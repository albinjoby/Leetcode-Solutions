class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        length = len(code)
        res = [0] * length
        
        if k == 0:
            return res

        for i in range(length):
            if k > 0:
                for j in range(i+1,i+1+k):
                    j = j % length
                    res[i] += code[j]
            else:
                for j in range(i-1,i-1-abs(k),-1):
                    j = j % length
                    res[i] += code[j]

        return res