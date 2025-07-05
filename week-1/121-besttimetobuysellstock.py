"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""

def maxProfit(prices):
    max_profit = 0              # track max_profit
    lower = prices[0]           # track lower price
    
    for i in range(len(prices)):
        if prices[i] - lower > max_profit:      # if profit > max_profit then replace
            max_profit = prices[i] - lower
        elif prices[i] < lower:                 # if current price < lowest then replace
            lower = prices[i]
        else:
            continue
        
    return max_profit

    # explicit 2 pointer
    # l, r = 0, 1               # day 1, 2
    # max_profit = 0
    
    # while r < len(prices):                    # within array bounds
    #   if prices[l] < prices[r]:
    #       profit = prices[r] - prices[l]          # get max_profit
    #       max_profit = max(profit, max_profit)
    #   else:
    #       l = r               # update left pointer to right position since its smaller
    #   r = r + 1               # increment right pointer so we don't compare the same day
    
    # return max_profit
    
print(maxProfit([7,1,5,3,6,4])) # 5