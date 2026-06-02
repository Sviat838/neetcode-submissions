class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        earn = 0

        l = 0
        r = 1

        while r < len(prices):
            if prices[r] > prices[l]:
                earn = max(earn, prices[r] - prices[l])
            elif prices[r] < prices[l]:
                l = r
            r +=1
        return earn