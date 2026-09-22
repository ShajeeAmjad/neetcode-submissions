class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # brute force
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                if prices[j] - prices[i] > max_profit and i < j:
                    max_profit = prices[j] - prices[i]
        return max_profit
        