class Solution(object):
    def finalPrices(self, prices):
        res = [p for p in prices]
        stack = []

        for i in range(len(prices)-1,-1,-1):
            while stack and prices[stack[-1]] > prices[i]:
                stack.pop()
            
            res[i] = prices[i] - prices[stack[-1]] if stack else prices[i]
            stack.append(i)

        return res