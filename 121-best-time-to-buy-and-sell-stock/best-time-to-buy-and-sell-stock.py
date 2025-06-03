class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = 0
        for r, price in enumerate(prices):
            res = max(res, price-prices[l])
            if price < prices[l]:
                l = r
            
        return res