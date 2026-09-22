class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # brute force
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i, len(prices)):
        #         if prices[j] - prices[i] > max_profit and i < j:
        #             max_profit = prices[j] - prices[i]
        # return max_profit

        # optimal
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            # profit?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1
        return max_profit



        