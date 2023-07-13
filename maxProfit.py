class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxpro =  0
        while right < len(prices):
            currpro = prices[right] - prices[left]
            if prices[left] < prices[right]:
                maxpro = max(currpro, maxpro)
            else:
                left = right
            right += 1
        return maxpro
        
