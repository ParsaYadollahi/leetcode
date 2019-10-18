class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        s = b = 0
        max_profit = 0
        while (s < len(prices)):
            profit = prices[s] - prices[b]
            if b == s or prices[b] < prices[s]:
                s += 1
                if max_profit < profit:
                    max_profit = profit 
            else:
                b += 1
        
        return max_profit
            