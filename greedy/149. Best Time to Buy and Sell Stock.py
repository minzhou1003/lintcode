"""
149. Best Time to Buy and Sell Stock
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example
Given array [3,2,3,1,2], return 1.
"""

# O(n)
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if not prices or len(prices) <= 1:
            return 0
        minimum_price = sys.maxsize
        max_profit = 0
        for price in prices:
            current_profit = price - minimum_price
            if current_profit > max_profit: # track the largest profit
                max_profit = current_profit
            if current_profit < 0: # find a lower price
                minimum_price = price
        return max_profit