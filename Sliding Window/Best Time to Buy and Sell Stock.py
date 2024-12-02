'''
Author: Semyon Guretskiy
'''


'''
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different
day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

Solution:
    The solution uses a single pass through the prices array keeping track of:
    1. Minimum price seen so far (best buying opportunity)
    2. Maximum profit possible by selling at current price
    
    At each step:
    - Calculate potential profit by selling at current price
    - Update minimum price seen so far
    - Keep track of maximum profit found
    
    This approach works because:
    - We only care about buying at the lowest price before selling
    - For each selling day, we want the minimum buying price from previous days
    - We don't need to track all possible combinations, just the best one found

    Time Complexity: O(n) where n is the length of prices array
    Space Complexity: O(1) as we only use constant extra space
'''

def maxProfit(prices):
    # Handle empty input
    if not prices:
        return 0
        
    # Initialize tracking variables
    min_price = prices[0]    # Minimum price seen so far
    max_profit = 0          # Maximum profit possible
    
    # Iterate through prices starting from day 2
    for current_price in prices[1:]:
        # Try to sell at current price
        # Profit would be current price minus minimum buying price seen
        potential_profit = current_price - min_price
        max_profit = max(max_profit, potential_profit)
        
        # Update minimum price seen for future selling opportunities
        min_price = min(current_price, min_price)
            
    return max_profit

if __name__ == "__main__":
    # Test case: [7,1,5,3,6,4]
    # Expected output: 5 (buy at 1, sell at 6)
    prices = [7,1,5,3,6,4]
    print(maxProfit(prices))