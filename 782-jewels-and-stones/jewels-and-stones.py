class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = Counter(stones)
        stones = set(stones)
        res = 0
        for jewel in jewels:
            if jewel in stones:
                res += counter[jewel]
            
        return res