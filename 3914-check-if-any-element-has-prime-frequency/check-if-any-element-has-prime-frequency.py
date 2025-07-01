class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        primes = {
            0:False,
            1:False,
            }
        def isPrime(num: int) -> bool:
            if num in primes:
                return primes[num]
            
            for i in range(2,num-1):
                if num % i == 0:
                    primes[num] = False
                    return False
            primes[num] = True
            return True

        counter = Counter(nums)
        for num in counter:
            if isPrime(counter[num]):
                return True
            
        return False
