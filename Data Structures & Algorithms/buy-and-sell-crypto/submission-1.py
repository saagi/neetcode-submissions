class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        maxprofit=0
        for right in range(len(prices)): # right:2,3
            profit = prices[right]-prices[left] # -6, 4, 2
            if profit<0: # left = 1, 4<0, 2<4
                left=right# left = 1
            maxprofit = max(maxprofit,profit) # 0, 4
        return maxprofit

        