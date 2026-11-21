class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_value_index = 0
        highest_value_index = len(prices) - 1
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < prices[lowest_value_index]:
                lowest_value_index = i
                highest_value_index = i
            if prices[i] > prices[highest_value_index]:
                highest_value_index = i
            profit = prices[highest_value_index] - prices[lowest_value_index]
            if profit > 0:
                max_profit = max(profit, max_profit)
        return max_profit