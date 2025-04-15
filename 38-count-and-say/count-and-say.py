class Solution:
    def countAndSay(self, n: int) -> str:
        def compress(x,n):
            if n == 1:
                return x
            count = 0
            res = ""
            cur = x[0]
            for i in range(len(x)):
                if x[i] == cur:
                    count += 1
                else:
                    res += f"{count}{cur}"
                    count = 1
                    cur = x[i]

            res += f"{count}{cur}"
            
            return compress(res, n-1)
        
        return(compress("1",n))
