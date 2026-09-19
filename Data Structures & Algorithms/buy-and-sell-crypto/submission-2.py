class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        maxprofit=0
        for right in range(len(prices)):
            profit = prices[right]-prices[left]
            if profit<0:
                left=right
            maxprofit = max(maxprofit,profit)
        return maxprofit

        