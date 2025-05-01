class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def check(n,x):
            if x > 16:
                return False
                
            if n == 0:
                return True
            
            if n < 0:
                return False

            return(check(n - 3**x, x+1) or check(n, x+1))
    
        return check(n,0)