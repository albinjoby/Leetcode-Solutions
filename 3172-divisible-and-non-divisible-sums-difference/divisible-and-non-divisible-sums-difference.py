class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # return (sum([x for x in range(1,n+1) if x % m != 0])-sum([x for x in range(1,n+1) if x % m == 0]))

        num1 = (n * (n+1))//2
        num2 = (n * (n+1))//2

        for num in range(1,n+1):
            if num % m == 0:
                num1 -= num
            else:
                num2 -= num
            
        return num1 - num2
