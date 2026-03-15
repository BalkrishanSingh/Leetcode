class Solution:
    def maxProfit(self, prices: List[int]) -> int:  
        current_max_profit:int = 0
        current_cheapest: int = prices[0]
        for i in range(1, len(prices)):
            predicted_profit:int = prices[i]- current_cheapest
            if current_max_profit < predicted_profit:
                current_max_profit = predicted_profit   
            if current_cheapest > prices[i]:
                current_cheapest = prices[i]
             
        return current_max_profit

#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150