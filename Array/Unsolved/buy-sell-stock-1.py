class Solution:
    def maxProfit(self, prices: List[int]) -> int:  
        current_max_profit:int = 0
        for i in range(0, len(prices)):
            for j in range(i+1,len(prices)):
                predicted_profit:int = prices[j]-prices[i]
                if current_max_profit < predicted_profit:
                    current_max_profit = predicted_profit
        return current_max_profit

#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150